import ControlActorsAction from control_actors_action

class ControlActorsActionTwo(ControlActorsAction):
    
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = LEFT
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = RIGHT
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = UP
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = DOWN
        
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)