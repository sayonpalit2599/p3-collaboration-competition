# Collaboration-Competition 
Multi Agent Deep Deterministic Policy Gradients  MADDPG algorithm based agent for solving the multi agent Tennis Environment (Unity) as part of Udacity's Deep Reinforcement Nanodegree by <a href = 'https://github.com/sayonpalit2599/'>Sayon Palit</a> 
## Project Environment
* For this project we work with Unity's <strong>Tennis</strong> environment

 <img src = "https://video.udacity-data.com/topher/2018/May/5af7955a_tennis/tennis.png">

* In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01. Thus, the goal of each agent is to keep the ball in play.

* The observation space consists of 8 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation. Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping.

### Solving the Environment
* The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents). Specifically,

	* After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 2 (potentially  
	  different) scores. We then take the maximum of these 2 scores.
	* This yields a single score for each episode.

<b>```The environment is considered solved, when the average (over 100 episodes) of those scores is at least +0.5.```</b>

## Requirements
### Getting Started
To run the codes, follow the next steps:
* Create a new environment:
	* __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	* __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
* Perform a minimal install of OpenAI gym
	* If using __Windows__, 
		* download swig for windows and add it the PATH of windows
		* install Microsoft Visual C++ Build Tools
	* then run these commands
	```bash
	pip install gym
	```
* Download this repository or clone it
	```bash
	git clone https://github.com/sayonpalit2599/p3-collaboration-competition/
	```
* Install the dependencies under the folder python/
```bash
	cd python
	pip install .
```
* Create an IPython kernel for the `drlnd` environment
```bash
	python -m ipykernel install --user --name drlnd --display-name "drlnd"
```
* Download the Unity Environment specific to your operating system
	* [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)
	* [Mac OSX](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
	* [Windows (32-bits)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)
	* [Windows (64 bits)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)

* Start jupyter notebook from the root of this python codes
```bash
jupyter notebook
```
* Once started, change the kernel through the menu `Kernel`>`Change kernel`>`drlnd`
* If necessary, inside the ipynb files, change the path to the unity environment appropriately

* Follow the instructions in `Tennis-v2.0.ipynb` to train the agent and see the performance of the agent.

* <strong>`It is recommended to use a GPU for running this code`</strong>
## Results
<img src = "https://github.com/sayonpalit2599/p3-collaboration-competition/blob/master/plot.jpg" alt = "result">

* The current model solves the environment in approx ~1906 epsiodes on average with an ` NVIDIA GTX1050TI ` and 
`Intel i8750H`.
