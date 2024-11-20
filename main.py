#Breaking down of the project into 7 parts
  # Part 1 : Creating a snake body
  # Part 2 : Move the snake body
  # Part 3 : Control the snake
  # Part 4 : Detect collision with food
  # part 5 : Create a scoreboard
  # Part 6 : Detect collision with wall
  # Part 7 : Detect collision with tail

from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

# creating Screen object
screen = Screen()

# settiing the game title
screen.title("SNAKE GAME")

# setting up the screen width and height
screen.setup(600,600)
# setting the screen background colour
screen.bgcolor("black")

# turning off the animation
screen.tracer(0)

# Part 1 :
snakes = Snake()
snakes.create_snake()

# Creating food 
food = Food()

# Part 5
scoreboard = ScoreBoard()

# Part 3 :
screen.listen()
screen.onkey(snakes.up, "w")   
screen.onkey(snakes.down, "s")
screen.onkey(snakes.right, "d")
screen.onkey(snakes.left, "a")

# Part 2 :
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()
    
    # Part 4 :   
    if snakes.segments[0].distance(food) < 15:
      scoreboard.increase_score()
      snakes.extend()
      food.refresh()
     
    # Part 6 : 
    x = snakes.segments[0].xcor()
    y = snakes.segments[0].ycor()
    if x > 290 or x < -300 or y > 301 or y < -290:
      scoreboard.gameover()
      game_on = False
      
    # Part 7 :
    for segment in snakes.segments[1:]:
      if snakes.segments[0].distance(segment) < 7:
        scoreboard.gameover()
        game_on = False
          
screen.exitonclick()