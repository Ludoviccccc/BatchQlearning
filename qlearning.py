import torch
import torch.nn
import torch.nn.functional as F
import os
import matplotlib.pyplot as plt
import numpy as np
from Qfunc import Q
#from agent import agent
def qlearn(buffer,
           batch_size,
           M,
           N,
           K,
           Qvalue,
           agent,
           optimizerQ,
           env,
           n_epochs,
           loadpath,
           loadopt, 
           gamma = .9,
           freqsave=100,
           epsilon = 0.1,
           start = 0
           ):
    Loss = torch.nn.MSELoss()
    listLossQ = []
    listRetour = []
    Qprim = Q(env, agent)
    def swap():
        Qprim.load_state_dict(Qvalue.state_dict())
    def collection(M):
        #choose some policy for the collection like the greedy one
        init_samp = {"state": [],
                     "action": [],
                     "new_state":[],
                     "reward": []}
        init_samp["state"] = torch.randint(0,env.Nx*env.Ny,(M,))  
        init_samp["action"]  = agent.amax_epsilon(Qvalue,init_samp["state"])
        init_samp["new_state"], init_samp["reward"] = env.transitionvec(init_samp["action"], init_samp["state"])
        buffer.store(init_samp)
    def updateQ(Samp):
        target = Samp["reward"] + gamma*Qprim.Qmax(Samp["new_state"])
        optimizerQ.zero_grad()
        pred = Qvalue(Samp["state"],Samp["action"]).squeeze()
        loss = Loss(pred.squeeze(),target.squeeze())
        loss.backward()
        optimizerQ.step()
        listLossQ.append(loss.detach().to("cpu"))
################################################################
    for i in range(start,n_epochs+1):
        swap()
        collection(M)
        for j in range(N):
            Samp = buffer.sample(batch_size)
            for k in range(K):
                 updateQ(Samp)
        print(f"i = {i}, n = {j},k={k}")
        if i%10==0 and i>0:
            torch.save(Qvalue.state_dict(), os.path.join(loadpath,f"q_load_{i}_{j}.pt"))
            torch.save(optimizerQ.state_dict(), os.path.join(loadopt,f"opt_q_load_{i}_{j}.pt"))
            list_retour, it = test(Qvalue,agent, env, epsilon =epsilon)
            retour = list_retour[0]
            listRetour.append(retour)
            plt.plot(listRetour, label="Retour")
            plt.xlabel("epoch")
            plt.title("Retour au premier état de l'episode en fonction de l'epoch")
            plt.legend()
            plt.savefig(os.path.join("plot","retour"))
            plt.close()
            print("retour", retour)
            print("nombre iterations", it)
    return None 
def test(Qvalue,
         agent,
         env,
         epsilon, 
         plot = False,
         gamma = .9,
         graph = False
         ):
    i = 0
    idx = torch.randint(0,env.Nx*env.Ny-len(env.obstacles_encod),(1,)).item()
    s = [a for a in range(env.Nx*env.Ny) if a not in env.obstacles_encod][idx]
    s = 31
    agent.epsilon = epsilon
    k = 0
    list_recompense = []
    if plot:
        if graph:
            env.grid(s,name=os.path.join("image",str(i)))
    while True:
        a = agent.amax_epsilon(Qvalue,[s])[0]
        sp,R = env.transitionvec(torch.Tensor([a]),torch.Tensor([s]))
        s = sp
        i+=1
        if plot:
            if graph:
                env.grid(int(s[0]),name=os.path.join("image",str(i)))
            else:
                env.grid(int(s[0]))
        list_recompense.append(R.item()*(gamma**k))
        k+=1
        if s==env.G:
            break
    list_retour = [sum(list_recompense[i:]) for i in range(len(list_recompense))]
    print(f"{i} pas de temps")
    return list_retour, i
