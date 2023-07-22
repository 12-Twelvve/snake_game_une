"""
You can import modules if you need
NOTE:
your code must function properly without 
requiring the installation of any additional 
dependencies beyond those already included in 
the Python package une_ai
"""
# import ...
import math
import random 
import numpy as np
from queue import Queue

from une_ai.models import GridMap

# Here you can create additional functions
# you may need to use in the agent program function

# environment grid model
env_col = 64
env_row = 48
# model
environment_map = GridMap(env_col, env_row, None)

DIRECTION = ['up','down','left','right']
MOVE_DIRECTION = {
    'up':"move-up",
    'down':"move-down",
    'left':"move-left",
    'right':"move-right"
}

def bfs_shortest_path_test(grid_map, start, target, body, obstacle, nearest_distance):
    # Implement Breadth-First Search to find the shortest path from start to target
    queue = Queue()
    queue.put((start, []))
    visited = set()
    while not queue.empty(): 
        (x, y), path = queue.get()
        if (x, y) == target:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            optimal_path=[]
            min_distance = nearest_distance
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                distance = manhattan_distance((new_x, new_y), target)
                if distance <= min_distance:
                    min_distance = distance
                    optimal_path.append((new_x, new_y))
            for new_x, new_y  in optimal_path:  
                try:
                    if (grid_map.get_item_value(new_x, new_y) is None or grid_map.get_item_value(new_x, new_y) == 'X' )and (new_x, new_y) not in visited:
                        if not obstacle_collision_detected(obstacle, (new_x, new_y)) and not own_body_collision_detected(body, (new_x, new_y)):
                            queue.put(((new_x, new_y), path + [(new_x, new_y)]))
                except:
                    pass
    return None


def manhattan_distance(point1, point2):
    # Calculate the Manhattan distance between two points
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def nearest_food(food_sources, cur_location, body, obstacle):
    # Find the nearest food source and its location
    nearest_distance = float('inf')
    nearest_food_location = None
    for food_x, food_y, _ in food_sources:
        distance = manhattan_distance((food_x, food_y), cur_location)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_food_location = (food_x, food_y)
    if nearest_food_location:
        # Find the shortest path from the current location to the nearest food
        path_to_food = bfs_shortest_path_test(environment_map, cur_location, nearest_food_location, body, obstacle, nearest_distance)
        return path_to_food
    else:
        return None

def obstacle_collision_detected(obstacle, new_location):
        if new_location in obstacle:
            return True
        return False

def own_body_collision_detected(body, new_location):
    if new_location in body:
        return True
    return False
def food_detected(foods, new_location):
    if new_location in [(food_x, food_y) for food_x, food_y, _ in foods]:
        return True
    return False

def future_state(model, cur_location, direction, obstacles, body, foods):
    offset = {
        # width, height
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0)
    }
    cur_x, cur_y = cur_location
    new_x, new_y = (cur_x + offset[direction][0], cur_y + offset[direction][1])
    try:
        value = model.get_item_value(new_x, new_y)
        new_location = (new_x, new_y)
    except:
        # if here it means that the next location will be out of bounds
        # so that's a wall
        value = 'W'
        new_location = None

    # food
    if food_detected(foods, new_location):
        value = 'F'
        return value, new_location
    # obstacle
    if obstacle_collision_detected(obstacles, new_location):
        value = 'O'
        new_location  = None
    # own body
    elif own_body_collision_detected(body, new_location):
        value = 'B'
        new_location = None
    else:
        result = nearest_food(foods, cur_location, body, obstacles)
        if result is not None and new_location == result[0]:   
            value = "K"

    return value, new_location

def inverse_direction(dir):
    if dir == 'up':
        return 'down'
    elif dir == 'left':
        return 'right'
    elif dir == 'down':
        return 'up'
    elif dir =='right':
        return 'left'
    else:
        return None

def test_behaviour(percepts, actuators):
    actions = []
    # Get the current position of the snake's head
    curr_direction = actuators['head']
    current_position = percepts['body-sensor'][0]
    body = percepts['body-sensor']
    food_sources = percepts['food-sensor']
    obstacles = percepts['obstacles-sensor']
    # if open mouth
    if actuators['mouth'] =='open':
        actions.append('close-mouth')
    # we can also update the current cell as visited
    environment_map.set_item_value(current_position[0], current_position[1], 'X')
    # check for future obstacle 
    # Initialize the list of valid directions
    valid_directions = []
    default_valid_direction = []
    # Check all possible directions
    temp_Direction = DIRECTION.copy()
    temp_Direction.remove(inverse_direction(curr_direction))
    random.shuffle(temp_Direction   )
    for direction in temp_Direction:
        future_state_value, _ = future_state(environment_map, current_position, direction, obstacles, body, foods=food_sources)
        if future_state_value == 'F':
            actions.append(MOVE_DIRECTION[direction])
            actions.append('open-mouth')
            return actions
        elif future_state_value =='K':
            actions.append(MOVE_DIRECTION[direction])
            return actions
        elif future_state_value != 'W' and future_state_value != 'O' and future_state_value != 'B':
            valid_directions.append(MOVE_DIRECTION[direction])
            # if future_state_value != 'X':
            #     # Add the direction to the list of valid directions
            #     valid_directions.append(MOVE_DIRECTION[direction])
            # else:
            #     default_valid_direction.append(MOVE_DIRECTION[direction])
    return default_valid_direction + valid_directions + actions

"""
TODO:
You must implement this function with the
agent program for your snake agent.
Please, make sure that the code and implementation 
of your agent program reflects the requirements in
the assignment. Deviating from the requirements
may result to score a 0 mark in the
agent program criterion.

Please, do not change the parameters of this function.
"""
def snake_agent_program(percepts, actuators):
    action = []
    # Apply the test_behaviour function
    actions = test_behaviour(percepts, actuators)
    return actions
