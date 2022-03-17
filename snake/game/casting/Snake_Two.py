from game.casting.snake import Snake
import constants
from game.casting.actor import Actor
from game.shared.point import Point

class snake_two(Snake):

    def _prepare_body(self):
        x = int(constants.MAX_X / 2.5)
        y = int(constants.MAX_Y / 2.5)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE + 5, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = self.get_head_color() if i == 0 else self.get_body_color()

            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def get_body_color(self):
        return constants.RED