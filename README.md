# US-states-game

This is a Python-based interactive game where the user is challenged to name all 50 U.S. states. As states are guessed correctly, they are displayed on a blank map of the U.S. The game allows the user to input their guesses and provides the ability to save a list of states the user has yet to guess.

## Features
- **Interactive map**: Users can visually see which states they have correctly guessed on a U.S. map.
- **Title case guessing**: The game accepts state names in a case-insensitive manner and converts input to title case.
- **Save missing states**: If the user exits the game early, a `.csv` file named `states_to_learn.csv` is generated, listing all the states the user didn't guess.
- **Coordinate-based display**: Correctly guessed states appear in their correct positions on the map.

## How It Works
1. The user is prompted to guess the name of a U.S. state.
2. If the state is guessed correctly, the name of the state is displayed on the U.S. map at the correct geographical location.
3. The game continues until all 50 states are guessed or until the user chooses to exit.
4. If the user exits early, a CSV file (`states_to_learn.csv`) is generated containing the names of the states the user did not guess.

## Dependencies
- `turtle`: Used to display the U.S. map and place the correct guesses on the screen.
- `pandas`: Used to read and manipulate data from CSV files.
- A CSV file named `50_states.csv` containing the names and coordinates of each state's position on the map.
  - The CSV file should have the following structure:
    ```plaintext
    state,x,y
    Alabama,139,-77
    Alaska,-450,-250
    Arizona,-161,14
    ...
    ```
