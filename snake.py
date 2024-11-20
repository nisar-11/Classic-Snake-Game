from turtle import Turtle  # Import the Turtle class from the turtle module

# Constants for initial snake position and movement
X_POSITION = [0, -20, -40]  # Initial positions of the snake segments
MOVE_FORWARD = 20  # Distance the snake moves forward each step
UP = 90  # Heading value for up direction
DOWN = 270  # Heading value for down direction
RIGHT = 0  # Heading value for right direction
LEFT = 180  # Heading value for left direction

# Define the Snake class
class Snake:
    def __init__(self) -> None:
        # Initialize the snake as a list of segments
        self.segments = []
    
    def create_snake(self):
        """
        Creates the initial snake body with three segments.
        Each segment is a square-shaped Turtle object.
        """
        for index in range(3):
            # Create a new segment
            segment = Turtle("square")
            segment.penup()  # Lift the pen to prevent lines from being drawn
            segment.color("white")  # Set the color of the segment to white
            segment.goto(X_POSITION[index], 0)  # Position the segment
            self.segments.append(segment)  # Add the segment to the snake
    
    def extend(self):
        """
        Extends the snake by adding a new segment at the position of the last segment.
        """
        segment = Turtle("square")  # Create a new segment
        segment.penup()  # Lift the pen to prevent drawing
        segment.color("white")  # Set the color of the segment to white
        # Position the new segment at the end of the snake
        self.x = self.segments[-1].xcor()
        self.y = self.segments[-1].ycor()
        segment.goto(self.x - 20, self.y)  # Place the new segment 20 units behind the last segment
        self.segments.append(segment)  # Add the new segment to the snake
    
    def move(self):
        """
        Moves the snake forward by shifting the position of each segment.
        The last segment moves to the position of the second-last segment, and so on.
        The head moves forward in its current direction.
        """
        # Start from the last segment and move each to the position of the segment before it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        # Move the head forward
        self.segments[0].forward(MOVE_FORWARD)
    
    def up(self):
        """
        Changes the direction of the snake's head to up (90 degrees) if it is not currently moving down.
        """
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
        """
        Changes the direction of the snake's head to down (270 degrees) if it is not currently moving up.
        """
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def right(self):
        """
        Changes the direction of the snake's head to right (0 degrees) if it is not currently moving left.
        """
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    
    def left(self):
        """
        Changes the direction of the snake's head to left (180 degrees) if it is not currently moving right.
        """
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
