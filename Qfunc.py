import torch.nn as nn
from torch.nn.utils.rnn import pad_sequence
import torch
class Q(nn.Module):
    def __init__(self,env,agent):
        super(Q,self).__init__()
        self.Nx = env.Nx
        self.Ny = env.Ny
        self.Na = env.Na
        self.agent = agent
        self.linear1 = nn.Linear(self.Ny*self.Nx + self.Na,16)
        self.linear2 = nn.Linear(16,16)
        self.linear3 = nn.Linear(16,1)
        self.actv = nn.ReLU()
        self.env = env
        self.states_encod = torch.eye(self.Nx*self.Ny).unsqueeze(0)
        self.actions_encod = torch.eye(self.Na).unsqueeze(0)
    def representation(self,state):
       return  pad_sequence([self.states_encod[0,:,int(i)] for i in state]).permute(1,0)
    def representationaction(self,action):
       return  pad_sequence([self.actions_encod[0,:,int(i)] for i in action]).permute(1,0)
    def forward(self, s,a):
        x = torch.cat((self.representation(s),self.representationaction(a)),dim=1)
        out = self.linear1(x)
        out = self.actv(out)
        out = self.linear2(out)
        out = self.actv(out)
        out = self.linear3(out)
        return out
    def Qmax(self,state_vec):
        return torch.Tensor([max(self.__call__([s]*self.Na, torch.arange(self.Na)).detach().squeeze()) for s in state_vec])

    #def amax_epsilon(self,state_vec, epsilon):
    #    out = []
    #    for s in state_vec:
    #        if torch.bernoulli(torch.Tensor([epsilon])):
    #            out.append(torch.randint(0,self.Na,(1,))[0])
    #        else:
    #            out.append(torch.argmax(self.__call__([s]*self.Na, torch.arange(self.Na)).detach().squeeze()))
    #    return out

