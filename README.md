# rlcourse-march-31-h-aboutalebi
rlcourse-march-31-h-aboutalebi created by GitHub Classroom
In this work I have reimplemented some of the experiments of the paper "Multi-agent Q-Learning of Channel Selection in Multi-user Cognitive Radio Systems (slides of my work is available in tember copy.pdf file):
A Two by Two Case". I have also attached the slides and the source code of my results.
So, we first tried to show that as the time passes the probability of chossing channel 1 decreases by one agent and the probability of chossing the same channel increases for the other agent:

![figure_2](https://cloud.githubusercontent.com/assets/5707322/24586951/6214cd8c-177a-11e7-9362-5b9703fc0fe2.png)
As it can be seen in this case the probaility of chossing channel 1 decreases for one agent and increases for the other agent. So, this encourages the result we proved that there is not going to be collision in the future. Here we have given same value two channel 1 and 2.

If we give higher value to channel 1, we see that it takes more time for convergence:
![figure_1](https://cloud.githubusercontent.com/assets/5707322/24586943/3fc2a380-177a-11e7-98d6-29e50520af6e.png)
This time the value of channel 1 is 20 times the value of channel 2.

This two graphs shows the eqiublirum graphs:
As it was mentioned the region 1 and 3 are nash equiblirium, and as it can be seen the trajectories finally converge to one of these region which advocate the result that we will converge


![figure_3](https://cloud.githubusercontent.com/assets/5707322/24586982/18a6c3c0-177b-11e7-8d1a-45a5b1c30924.png)

![figure_4](https://cloud.githubusercontent.com/assets/5707322/24586985/21510396-177b-11e7-8695-7924f6e5fe42.png)
The arrows shows the path of trajectory
