import torch
class Agent:
    def __init__(self, Na,Nx,Ny,epsilon):
        self.Na = Na
        self.Nx = Nx
        self.Ny = Ny
        self.epsilon = epsilon
    def amax_epsilon(self,Q,state_vec):
          out = []
          for s in state_vec:
              if torch.bernoulli(torch.Tensor([self.epsilon])):
                  out.append(torch.randint(0,self.Na,(1,))[0])
              else:
                  out.append(torch.argmax(Q([s]*self.Na, torch.arange(self.Na)).detach().squeeze()))
          return out

