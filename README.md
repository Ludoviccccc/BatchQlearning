# Implementation of a parallel Qlearning algorithm with pyTorch
I follow the course CS 285 at UC Berkeley.
![alt text](AlgoImage.png)
The environement is a grid of size $(n_x,n_y)$. An agent has to reach a point called G.<br>
Integers N and K are the number of iterations for the loop 2 of the collection of the datapoints from the buffer and for the loop 3 with the batch sampling and the update. The process is repeted $n_{epochs}$ times.<br>

d (-1, 0)<br>
[[0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 6. 0.]<br>
 [0. 0. 1. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]]<br>
d (-1, 0)<br>
[[0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 1. 0. 6. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]]<br>
d (0, 1)<br>
[[0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 1. 6. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]]<br>
d (0, 1)<br>
[[0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 1. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]<br>
 [0. 0. 0. 0. 0. 0.]]<br>
4 pas de temps <br>

* The file qlearning.py implements the loop in a function called qlearn.
* The file Qfunc.py implements the action-value network Q.
* The file Buffer.py implements the buffer containing batchs (s,a,s',r)
* The file main.py calls qlearn nad gives values for $K$ and $N$.
