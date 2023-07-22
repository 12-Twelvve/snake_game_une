# Assignment 1 - Student's Report

Author: Pooja Timalsina 
Student ID: 220245940

## Class of the Agent Program

The agent program falls into the class of goal-based agents. A goal-based agent is one that decides what to do by considering its current state and the desired goals. It employs a search algorithm or planning mechanism to determine a sequence of actions that will lead it from the current state to a state that satisfies its goals. In this case, the agent's goal is to find and consume food while avoiding obstacles and its own body. The agent uses a Breadth-First Search (BFS) algorithm to find the shortest path to the nearest food source, making it a goal-based agent as it pursues the goal of reaching the food source efficiently.
	
## AI Techniques Considered

Model-based agents use internal models to simulate outcomes, creating an accurate model for the complex snake game proved challenging. Similarly, utility-based agents, which aim to maximize a utility function, were unnecessary for the straightforward objectives of the game (eating food and avoiding collisions).

By leveraging BFS, the goal-based snake agent can efficiently explore the grid, locate nearby food sources, and plan its path accordingly. This goal-directed behavior aligns with the agent's primary objective of finding and consuming food while maintaining a collision-free trajectory. Overall, the chosen goal-based approach using BFS offers a robust and effective solution to tackle the snake game's challenges.

## Reflections

Throughout the problem-solving and implementation phases, we encountered several challenges that demanded our attention.

The first challenge was integrating the agent into the game environment required thoughtful design and testing. We meticulously set up sensors, actuators, and interactions with the game logic to ensure smooth and seamless integration.

Another critical aspect was collision avoidance. We meticulously crafted a robust decision-making process, incorporating comprehensive collision detection mechanisms. This ensured that the agent could effectively avoid obstacles and navigate its own body, mitigating the risk of unintended collisions.

Moreover, optimizing the pathfinding efficiency to locate the nearest food source. We successfully fine-tuned the BFS algorithm to handle the large game grid efficiently, enabling the agent to find optimal paths to food sources quickly.

To overcome these challenges, we conducted thorough testing and debugging, refining the agent's performance and behavior.
