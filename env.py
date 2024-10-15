import torch
import torch.nn.functional as F
from torch.nn.utils.rnn import pad_sequence
import torch.nn as nn
import numpy as np

class grid:
    """
    Envirnonement grille sur laquelle se deplace l'agent jusqu'à atteindre le point G
    """
    def __init__(self,Nx,Ny, G = 50,obstacles_encod = torch.Tensor([])):
        assert(0<=G<Nx*Ny)
        self.actions = [(0,1), (0, -1), (1, 0), (-1, 0),(1,1),(1,-1),(-1,-1),(-1,1)]
        self.Na = len(self.actions)
        self.Nx = Nx
        self.Ny = Ny
        self.G = G
        self.obstacles_encod = obstacles_encod
    def transitionvec(self,a,s):
        "a un est un torch tensor à une dimension"
        "s un est un torch tensor à une dimension"
        couples = {0:s//self.Ny,1:s%self.Ny}
        mouv1,mouv2 = self.representation_action(a)
        InGrid =(couples[0]+mouv1>=0)*(couples[0]+mouv1<self.Nx)*(couples[1]+mouv2>=0)*(couples[1]+mouv2<self.Ny)
        NotInGrid = InGrid==False
        state_not_in_obst = torch.isin((couples[0]+mouv1)*self.Ny+couples[1]+mouv2, self.obstacles_encod) ==False
        couples2 = {0:couples[0]+mouv1*InGrid*state_not_in_obst,
                    1:couples[1]+mouv2*InGrid*state_not_in_obst}
        newstate = couples2[0]*self.Ny+couples2[1]
        reward = (newstate==self.G)+ NotInGrid*(-1)+(s==newstate)*(-1)+state_not_in_obst*(-1)
        return newstate,reward
    def grid(self,s):
        assert(type(s)==int)
        assert(0<=s<=self.Nx*self.Ny)
        T = torch.zeros((self.Nx,self.Ny))
        T[self.G//self.Ny, self.G%self.Ny] = 6
        T[s//self.Ny, s%self.Ny] = 11
        for p in self.obstacles_encod:
            #print("p",p)
            T[int(p)//self.Ny, int(p)%self.Ny] = -1
        print(T)
    def representation_action(self,a):#tensor to describe the player movements
        return torch.Tensor([self.actions[int(i)][0] for i in a]), torch.Tensor([self.actions[int(i)][1] for i in a])
