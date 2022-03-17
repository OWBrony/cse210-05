import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score and moves the food if a snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        snakeTwo = cast.get_first_actor("snake2")
        headTwo = snakeTwo.get_head()
        head = snake.get_head()

        if self.collides(head.get_position(), food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            # score.add_points(points)
            food.reset()

        if self.collides(headTwo.get_position(), food.get_position()):
            points = food.get_points()
            snakeTwo.grow_tail(points)
            # score.add_points(points)
            food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
#Assign  parts of first snake to variables
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
       

#Assign parts of second snake to variables
        snakeTwo = cast.get_first_actor("snake2")
        segmentsTwo = snakeTwo.get_segments()[1:]
        headTwo = snakeTwo.get_segments()[0]


        for segment2 in segmentsTwo:
            if self.collides(head.get_position(), segment2.get_position()):
                self._is_game_over = True

        for segment in segments:
            if self.collides(headTwo.get_position(),segment.get_position()):
                self._is_game_over = True


    def collides(self, pt1, pt2):
        threshold = 15
        if pt1.get_x() - threshold  < pt2.get_x() and pt1.get_x() + threshold > pt2.get_x() and pt1.get_y() - threshold < pt2.get_y() and pt1.get_y() + threshold > pt2.get_y():
            return True
        else:
            return False


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            snakeTwo = cast.get_first_actor("snake2")
            segments = snake.get_segments()
            segmentsTwo = snakeTwo.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segmentsTwo:
                segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)