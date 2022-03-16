# cycle-game
A game about cutting off the other player.

Need to have two snakes.
Player's tail continues to grow over time.
Players try to get the other to cross their tail.
Crossing the other's tail will result in a game over (snakes turn white)

Alter keyboard input (awsd for player 1 and jikl form player 2).
add different color for player 2.
add different tracking for player 2 (length, others?).

Movement (Bryce)
different color (James)



Implementation as of 3/16/2022

Changes from base snake game:

main.py
Implementation of more actors(badsnake) via cast in the main.py file

Snake_Two.py
Added Snake_Two.py file that implements a second snake. Color of second snake is changed to red.

control_actors_action_two.py
Added control_actors_action_two.py file that implements movement for second snake


draw_actors_action.py
Added code to draw_actors_action.py to assign parts of the second snake to variables and then implement them in game. ( Incomplete because game functionality is incomplete)

handle_collisions_action.py
Added code to assign parts of the second snake to variables and then implement them in game (Incomplete because game functionality is incomplete)


Things to improve
James - Implement color change. Although it is implemented for the second snake, I have a feeling there is a better way to do it. It would require a rethinking of the classes in the project. By changing the snake class and the parameters you pass into it, you can pass in the color of the snake using a parameter when you instantiate the snake. 

Fix collision so that both snakes will die if collided with each other. 

Fix eating so that both snakes will grow when they run into the fruit

Implement scoring. 






Can change the color of 
