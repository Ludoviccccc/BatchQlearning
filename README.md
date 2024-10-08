# Implementation of a parallel Qlearning algorithm
I follow the course CS 285 at UC Berkeley.
![alt text](AlgoImage.png)
The environement is a grid of size $(n_x,n_y)$
An agent has to reach a point called G.

d (-1, 0)
[[0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 6. 0.]<br>
 [0. 0. 1. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]]<br>
d (-1, 0)
[[0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 1. 0. 6. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]]<br>
d (0, 1)
[[0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 1. 6. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]]<br>
d (0, 1)
[[0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 1. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]]<br>
4 pas de temps

