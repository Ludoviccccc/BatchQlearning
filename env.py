import torch
import torch.nn.functional as F
from torch.nn.utils.rnn import pad_sequence
import torch.nn as nn
import numpy as np

class grid:
    """
    Envirnonement grille sur laquelle se deplace l'agent jusqu'à atteindre le point G
    """
    def __init__(self,Nx,Ny, G = 50):
        assert(0<=G<Nx*Ny)
        self.actions = [(0,1), (0, -1), (1, 0), (-1, 0),(1,1),(1,-1),(-1,-1),(-1,1)]
        self.Na = len(self.actions)
        self.Nx = Nx
        self.Ny = Ny
        self.G = G
    def transition(self,a,s):
        assert(0<=s<self.Nx*self.Ny)
        d = self.actions[a]
        s_couple = (s//self.Ny, s%self.Ny)
        print("d", d)
        if self.Nx>s_couple[0]+ d[0]>=0 and self.Ny>s_couple[1]+d[1]>=0:
            sp = (s_couple[0]+ d[0], s_couple[1]+d[1])
            assert(0<=sp[0]*self.Ny+sp[1]<self.Nx*self.Ny)
            s = sp[0]*self.Ny+sp[1]  
        R = (s==self.G)
        return s,R
    def transitionvec(self,a,s):
        "a un est un torch tensor à une dimension"
        "s un est un torch tensor à une dimension"
        couples = {0:s//self.Ny,1:s%self.Ny}
        mouv1,mouv2 = self.representation_action(a)
        A =(couples[0]+mouv1>=0)*(couples[0]+mouv1<self.Nx)*(couples[1]+mouv2>=0)*(couples[1]+mouv2<self.Ny)
        couples2 = {0:(couples[0]+mouv1*A),
                    1:(couples[1]+mouv2*A)
                    }
        newstate = couples2[0]*self.Ny+couples2[1]
        reward = (newstate==self.G)*A+(A*(-1)+1)*(-1)
        return newstate,reward
    def grid(self,s): #show the grid and the player
        assert(type(s)==int)
        assert(0<=s<=self.Nx*self.Ny)
        T = np.zeros((self.Nx,self.Ny))
        T[self.G//self.Ny, self.G%self.Ny] = 6
        T[s//self.Ny, s%self.Ny] = 1
        print(T)
    def representation_action(self,a):#tensor to describe the player movements
        return torch.Tensor([self.actions[int(i)][0] for i in a]), torch.Tensor([self.actions[int(i)][1] for i in a])
