# Implementation of a parallel Qlearning algorithm
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
4 pas de temps

