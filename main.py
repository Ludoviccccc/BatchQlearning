import torch
import torch.optim as optim
import torch.nn.functional as F
from torch.nn.utils.rnn import pad_sequence
import sys
from Qfunc import Q
from buffer import Buffer
from env import grid
import os
from qlearning import qlearn, test
import matplotlib.pyplot as plt
from agent import Agent
import json
if __name__=="__main__":
    with open("arg.json","r") as f:
        data = json.load(f)
    train = data["train"]
    test_mode = data["test_mode"]
    start = data["start"]
    epsilon = data["epsilon"]
    gamma = data["gamma"]
    nx = data["nx"]
    ny = data["ny"]
    G = data["G"]
    ob = torch.Tensor(data["ob"])
    lr = data["lr"]
    n_epochs = data["n_epochs"]
    batch_size = data["batch_size"]
    M = data["M"]
    N = data["N"]
    maxsize = data["maxsize"]
    K = data["K"] #nombre iterations descente de gradient pour le meme batch (s,a,r,s')
    loadpath = data["loadpath"]
    loadopt = data["loadopt"]
    na = data["na"]
    graph = data["graph"]




    env = grid(nx,ny,G = G, obstacles_encod = ob) 

    agent = Agent(na,nx,ny,epsilon)
    Qvalue = Q(env,agent)
    optimizerQ = optim.Adam(Qvalue.parameters(), lr = lr) 
    if start>0:
        Qvalue.load_state_dict(torch.load(os.path.join(loadpath,f"q_load_{start}_0.pt"), weights_only=True))
        optimizerQ.load_state_dict(torch.load(os.path.join(loadopt,f"opt_q_load_{start}_0.pt"), weights_only=True))
    bffer = Buffer(maxsize = maxsize)
    if train:
        qlearn(bffer,
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
               gamma = gamma,
               start = start)
    if test_mode:
        list_retour, nb_iterations = test(Qvalue,
                                            agent,
                                            env,
                                            epsilon = 0,
                                            plot = True,
                                            graph = graph)
        print(list_retour)
        plt.plot(list_retour, label="retour")
        plt.grid()
        plt.legend()
        plt.show()
