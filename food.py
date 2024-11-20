from turtle import Turtle  # Import the Turtle class from the turtle module
import random  # Import the random module for generating random positions

# Define the Food class that inherits from the Turtle class
class Food(Turtle):
    def __init__(self) -> None:
        # Initialize the parent Turtle class
        super().__init__()
        
        # Set the shape of the food to a circle
        self.shape("circle")
        
        # Lift the pen so the food object doesn't leave a trail when moving
        self.penup()
        
        # Scale down the size of the food object (default size is 20x20, reduced to 10x10 here)
        self.shapesize(0.5, 0.5)
        
        # Set the color of the food to orange
        self.color("orange")
        
        # Set the movement speed of the food object to the fastest setting
        self.speed("fastest")
        
    # Method to refresh the food's position randomly within the screen bounds
    def refresh(self):
        # Move the food to a random position within the range of -280 to 280 on both axes
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
