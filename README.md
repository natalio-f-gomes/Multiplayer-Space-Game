# Multiplayer-Space-Game

<p align="center">
  <img width="905" alt="Screenshot 2023-04-29 at 6 03 41 PM" src="https://user-images.githubusercontent.com/116610989/235325912-f72737aa-0a46-47a3-9318-0962964134ff.png">
</p>

This code is an implementation of a two-player space game using Pygame library. It creates a window, two spaceships, and allows them to shoot bullets at each other.

The Game class contains all the methods and attributes needed for the game. The __init__ method initializes Pygame, sets up the window, loads the images and sounds, and defines some constants.

The draw_window method draws the spaceships and bullets, updates the health bars, and the background of the window. The draw_winner method displays the winner of the game after it ends.

The handle_ship_movement method moves the spaceships according to the keyboard inputs. The shoot method creates bullets and handles collisions.

The main loop of the game is in the main function. It handles events, updates the positions of the spaceships and bullets, checks for collisions, and ends the game if a player's health is 0.
Installation

Clone the repository:

git clone https://github.com/natalio-f-gomes/Multiplayer-Space-Game.git

Install Pygame:

pip install pygame

Run the game:

python main.py

HAVE FUN


Contributions

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.


Credits

This game was created by Your Natalio Gomes. Thanks to the Pygame library for making it easy to create games in Python!
Shout out to Tech With Tim.
