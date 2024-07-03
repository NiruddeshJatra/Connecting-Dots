# Connecting Dots Game

## Overview
Connecting Dots is a fun and interactive game implemented using Python's Turtle and Pygame libraries. The game allows multiple players to connect dots on a grid, aiming to form squares. The player who forms the most squares wins the game.

## Features
- Multiple player support
- Customizable grid size
- Sound effects for various game actions
- Visual feedback for player turns and game results

## Installation
1. Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/).

2. Install the required libraries:
   ```sh
   pip install pygame
   pip install python-turtle
   ```

3. Clone or download this repository.

4. Place your sound files in a folder named `sound` within the same directory as the game script.

## Running the Game
Run the game script using Python:
```sh
python connect_dots_game.py
```

## How to Play
1. **Starting the Game:**
   - When the game starts, you'll be prompted to enter the number of players (minimum of 2 players).
   - Next, you'll be asked to enter the grid size (a number between 5 and 10).

2. **Playing the Game:**
   - Players take turns to connect dots by clicking on the screen.
   - When it's your turn, click on two adjacent dots to draw a line between them.
   - The goal is to form squares by connecting dots.

3. **Scoring:**
   - Each player aims to complete squares on the grid.
   - When a player completes a square, their player number is displayed inside the square.
   - The player who forms the most squares by the end of the game wins.

4. **Game End:**
   - The game ends when all possible squares have been formed.
   - The player with the most squares is declared the winner.

## Sound Effects
- **message_box.mp3**: Played when the game starts and after valid inputs.
- **error.wav**: Played for invalid inputs.
- **life_grand_background_music.mp3**: Background music played throughout the game.
- **end.wav**: Played when the game ends.
- **get_bonus.wav**: Played when a player completes a square.
- **click.wav**: Played when a line is drawn between dots.

## Game Over
When the game ends, the screen displays "GAME OVER" followed by the winning player's number.

## Notes
- Make sure your sound files are correctly named and placed in the `sound` directory.
- Ensure you have the necessary permissions to play sound files on your system.

## Credits
Built by Nasiful Alam.

Enjoy playing Connecting Dots with your friends!
