from une_ai.models import Agent
import numpy as np
class SnakeAgent(Agent):
    # DO NOT CHANGE THE PARAMETERS OF THIS METHOD
    def __init__(self, agent_program):
        # DO NOT CHANGE THE FOLLOWING LINES OF CODE
        super().__init__("Snake Agent", agent_program)

        """
        If you need to add more instructions
        in the constructor, you can add them here
        """
        
    """
    TODO:
    In order for the agent to gain access to all 
    the sensors specified in the assignment's 
    requirements, it is essential to implement 
    this method.
    You can add a single sensor with the method:
    self.add_sensor(sensor_name, initial_value, validation_function)
    """
    def add_all_sensors(self):
        # Sensor to store the snake's body segments as a list of tuples (x, y)
        self.add_sensor('body-sensor', [], lambda v: isinstance(v, list) and all(isinstance(segment, tuple) and len(segment) == 2 and all(isinstance(coord, int) for coord in segment) for segment in v))
        # Sensor to store food sources as a list of tuples (x, y, score)
        self.add_sensor('food-sensor', [], lambda v: isinstance(v, list) and all(isinstance(food, tuple) and len(food) == 3 and all(isinstance(coord , int) for coord in food[:2]) and isinstance(food[2], np.int64) for food in v))
        # Sensor to store obstacles as a list of tuples (x, y)
        self.add_sensor('obstacles-sensor', [], lambda v: isinstance(v, list) and all(isinstance(obstacle, tuple) and len(obstacle) == 2 and all(isinstance(coord, int) for coord in obstacle) for obstacle in v))
        # Sensor to store the remaining time before Game Over, measured in seconds
        self.add_sensor('clock', 0, lambda v: isinstance(v, int) and v >= 0)

    """
    TODO:
    In order for the agent to gain access to all 
    the actuators specified in the assignment's 
    requirements, it is essential to implement 
    this method.
    You can add a single actuator with the method:
    self.add_actuator(actuator_name, initial_value, validation_function)
    """
    def add_all_actuators(self):
        # Actuator to adjust the snake's head trajectory ('up', 'down', 'left', 'right')
        self.add_actuator('head', 'left', lambda v: v in ['up', 'down', 'left', 'right'])

        # Actuator to control the snake's mouth state ('open', 'close')
        self.add_actuator('mouth', 'close', lambda v: v in ['open', 'close'])

    """
    TODO:
    In order for the agent to gain access to all 
    the actions specified in the assignment's 
    requirements, it is essential to implement 
    this method.
    You can add a single action with the method:
    self.add_action(action_name, action_function)
    """
    def add_all_actions(self):
        self.add_action(
            'move-up',
            lambda: {'head':'up'} if not self.read_actuator_value('head') == 'down' else {}
            )
        self.add_action(
            'move-down',
            lambda: {'head':'down'} if not self.read_actuator_value('head') == 'up' else {}
            )
        self.add_action(
            'move-left',
            lambda: {'head':'left'} if not self.read_actuator_value('head') == 'right' else {}
            )
        self.add_action(
            'move-right',
            lambda: {'head':'right'} if not self.read_actuator_value('head') == 'left' else {}
            )
        self.add_action(
            'open-mouth',
            lambda: {'mouth':'open'} 
            )
        self.add_action(
            'close-mouth',
            lambda: {'mouth':'close'}
            )