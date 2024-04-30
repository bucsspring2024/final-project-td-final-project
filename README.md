[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14928615&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Runner Game
## CS110 Final Project  Spring, 2024 

## Team Member

 Thirandi Dandeniya 

***

## Project Description

Runner Game is a basic side scrolling game where players dodge obstacles to survive as long as possible. Jump in and see how long you can keep running!!!

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu
2. Moveable character
3. Obstacle collisions
4. Scrolling background
5. Game Over Screen

### Classes

- Controller Class: Manages all interactions and state updates; Handles events, updates models for collisions, and redraws the screen.
- Player Class: Handles player-specific things like jumping and gravity.


## ATP

ATP 1:
Test Description: Verify that user can jump when you click spacebar.
Test Steps:
    1. Start game to see main screen
    2. Click spacebar to jump
    3. Observe player's jump and return to ground
Expected Outcome: User should be able to jump and then return back to the ground.

ATP 2:
Test Description: Verifies if the game catches collisions when the player and obstacles meet, resulting in game over.
Test Steps:
    1. Start the game
    2. Allow the player to run into an obstacle without jumping
    3. Observe the game's response to the collision
Expected Outcome: When collision occurs, user should see game over screen.

ATP 3:
Test Description: User should be able to restart the game after seeing the game over screen.
Test Steps:
    1. Start the game and collide with an obstacle to reach the game over screen
    2. Click enter key to restart
    3. Check if game restarts and starts a new one
Expected Outcome: Clicking the enter key after the game over screen should allow the user to restart the game with no obstacles near them.

ATP 4:
Test Description: Game should initialize with all of the visual elements.
Test Steps:
    1. Start game
    2. The player and background visuals should be on the screen
Expected Outcome: Player and background should show up on the screen with no errors or delays.

ATP 5:
Test Description: Verify if the main menu lets the user start or quit the game.
Test Steps:
    1. Start the game
    2. Click enter to start the game
    3. Once you get back to the main menu, click the escape key to quit the game
Expected Outcome: Clicking the enter key at the main menu should start the game and clicking the escape key should close the game window.