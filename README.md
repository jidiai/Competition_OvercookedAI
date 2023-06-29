<img src="imgs/Jidi%20logo.png" width='300px'> 

# SJTU AI603 OvercookedAI Competition 上海交通大学 AI1603 课程竞赛

This repo provide the source code for the [SJTU AI603 coursework competition](http://www.jidiai.cn/compete_detail?compete=40)



## Multi-Agent Game Evaluation Platform --- Jidi (及第)
Jidi supports online evaluation service for various games/simulators/environments/testbeds. Website: [www.jidiai.cn](www.jidiai.cn).

A tutorial on Jidi: [Tutorial](https://github.com/jidiai/ai_lib/blob/master/assets/Jidi%20tutorial.pdf)


## Environment
The competition adopts an integrated version of [OvercookedAI games](https://github.com/HumanCompatibleAI/overcooked_ai)


### OvercookedAI-Integrated
<img src='https://jidi-images.oss-cn-beijing.aliyuncs.com/jidi/env98.gif' width=400>

- The integrated game contains three official maps, they are： 1. Forced Coordinatiom; 2. Coordination Ring; 3. Cramped Room
- The game proceed by putting both agents sequentially in these three maps and ask them to prepare orders by cooperating with the other player. The ending state in a map is followed by an initial state in the next map and the agent observation will be marked *new_map=True*
- Each map will be run twice with agent index switched. For example in map one, player one controls agent one and player two controls agent two and they switch position and re-start the map when reaching an end. Thus, two players will play on three maps for six rounds in total.
- Each map last for 500 timesteps. The total episode length of the integrated game is 2400.
- Each agent observation global game state, the agent index and the new map indicator. The gloabl game state includes:
  - players: position and orientation of two characters and the held objects.
  - objects: the information and position of objects in the map.
  - bounus orders
  - all orders
  - timestep:  timestep in the current map
- Each agent has six action choices, they are:
  - Move Up
  - Move Down
  - Move Right
  - Move Left
  - Stay Still
  - Interact
- We use the default reward shaping, that is +20 for each successful orders. We will sum up all rewards in all maps as the score for one episode.


## Quick Start

You can use any tool to manage your python environment. Here, we use conda as an example.

```bash
conda create -n overcookai-venv python==3.8  # or 3.9 We have tested for both
conda activate overcookai-venv
```

Next, clone the repository and install the necessary dependencies:
```bash
git clone https://github.com/jidiai/Competition_OvercookedAI.git
cd Competition_OvercookedAI
pip install -r requirements.txt
```

Finally, run the game by executing:
```bash
python run_log.py
```


## Navigation

```
|-- Competition_OvercookedAI               
	|-- agents                              // Agents that act in the environment
	|	|-- random                      // A random agent demo
	|	|	|-- submission.py       // A ready-to-submit random agent file
	|-- env		                        // scripts for the environment
	|	|-- config.py                   // environment configuration file
	|	|-- overcookedai_integrated.py  // The environment wrapper		      
	|-- utils               
	|-- run_log.py		                // run the game with provided agents (same way we evaluate your submission in the backend server)
```



## How to test submission

You can locally test your submission. At Jidi platform, we evaluate your submission as same as *run_log.py*

For example,

>python run_log.py --my_ai "random" --opponent "random"


---

## Ready to submit

Random policy --> *agents/random/submission.py*

solve the tasks with any method you like, e.g. rule-based, heuristic, RL, etc.
