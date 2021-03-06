from game.scripting.control_actors_action import ControlActorsAction 
import constants
from game.scripting.action import Action
from game.shared.point import Point

LEFT = Point(-constants.CELL_SIZE, 0)
RIGHT = Point(constants.CELL_SIZE, 0)
UP = Point(0, -constants.CELL_SIZE)
DOWN = Point(0, constants.CELL_SIZE)

class ControlActorsActionTwo(ControlActorsAction):
    
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j') and self._direction != RIGHT:
            self._direction = LEFT
        
        # right
        if self._keyboard_service.is_key_down('l') and self._direction != LEFT:
            self._direction = RIGHT
        
        # up
        if self._keyboard_service.is_key_down('i') and self._direction != DOWN:
            self._direction = UP
        
        # down
        if self._keyboard_service.is_key_down('k') and self._direction != UP:
            self._direction = DOWN
        
        snake = cast.get_first_actor("snake2")
        snake.turn_head(self._direction)