# Classic Snake Game  

## 🧑‍💻 Author  
- **MOHAMMED NISAR SHAREEF**  

## 🐍 Overview  
The **Classic Snake Game** is a Python-based recreation of the timeless snake game. The game is implemented using the `turtle` module, providing an interactive and engaging experience. Players control the snake, collect food to grow in size, and aim to achieve the highest score possible while avoiding collisions.

---

## 🚀 Features  
- **Dynamic Snake Movement**: The snake grows as it collects food.  
- **Food Generation**: Randomly placed food for the snake to consume.  
- **Score Tracking**: Displays the current score and keeps track of the highest score.  
- **Game Over Scenarios**:  
  - Collision with walls.  
  - Collision with the snake's own body.  
- **Keyboard Controls**:  
  - **W**: Move Up.  
  - **S**: Move Down.  
  - **D**: Move Right.  
  - **A**: Move Left.  

---

## 🎮 How to Play  
1. Clone this repository to your local machine.  
2. Run `main.py` in a Python environment.  
3. Use the keyboard controls to navigate the snake.  
4. Collect food to increase your score.  
5. Avoid colliding with the walls or the snake's tail.  
6. Try to beat the highest score!

---

## 🛠️ Project Breakdown  
The game is divided into several components:  
### 1. **Creating the Snake Body**  
   The snake starts with three segments arranged horizontally.  
### 2. **Snake Movement**  
   The snake moves in a continuous forward motion.  
### 3. **Snake Controls**  
   Players can change the direction using keyboard controls.  
### 4. **Food Generation**  
   Food appears randomly within the game boundary.  
### 5. **Scoreboard**  
   Displays the current score and updates the high score.  
### 6. **Collision Detection with Walls**  
   The game ends if the snake's head touches the boundary.  
### 7. **Collision Detection with Tail**  
   The game ends if the snake collides with its own body.

---

## 🖥️ Requirements  
- Python 3.8 or higher.  
- Turtle module (pre-installed with Python).  

---

## 📁 File Structure  
- `main.py`: Main game logic and flow.  
- `food.py`: Handles food creation and positioning.  
- `scoreboard.py`: Manages the scoreboard and high score tracking.  
- `snake.py`: Implements the snake's behavior and movement.  
- `data.txt`: Stores the high score persistently.  



