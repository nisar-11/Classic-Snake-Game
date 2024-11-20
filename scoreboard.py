from turtle import Turtle  # Import the Turtle class from the turtle module

# Define the ScoreBoard class that inherits from the Turtle class
class ScoreBoard(Turtle):
    def __init__(self) -> None:
        # Initialize the parent Turtle class
        super().__init__()
        
        # Initialize the player's current score to 0
        self.score = 0

        # Read the high score from a file called "data.txt"
        with open("data.txt") as data:
            self.highscore = int(data.read())  # Convert the stored value to an integer
        
        # Set up the scoreboard's appearance
        self.color("white")  # Set the text color to white
        self.hideturtle()  # Hide the turtle icon (only the text will be visible)
        self.penup()  # Lift the pen to prevent unwanted lines from being drawn

        # Position the scoreboard at the top center of the screen
        self.goto(0, 268)
        
        # Display the initial score and high score
        self.write(f"Score : {self.score} Highscore : {self.highscore}", 
                   False, "center", ("Arial", 20, "bold"))

    # Method to handle the game over scenario
    def gameover(self):
        # If the player's score is greater than the high score, update the high score
        if self.score > self.highscore:
            self.highscore = self.score  # Update the high score in memory
            # Save the new high score to "data.txt"
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")  # Write the new high score to the file
        
        # Move the turtle to the center of the screen
        self.home()
        
        # Display the "GAME OVER" message
        self.write("GAME OVER", False, "center", ("Arial", 24, "bold"))

    # Method to increase the score during the game
    def increase_score(self):
        self.score += 1  # Increment the score by 1
        self.clear()  # Clear the previous score display
        # Display the updated score and high score
        self.write(f"Score : {self.score}, Highscore : {self.highscore}", 
                   False, "center", ("Arial", 20, "bold"))
