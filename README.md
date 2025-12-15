# Hangman GUI Game

This project is a graphical user interface (GUI) implementation of the classic Hangman game. It is designed to be user-friendly and engaging for players of all ages.

## Project Structure

```
hangman-gui
├── src
│   ├── main.py               # Entry point of the application
│   ├── game
│   │   ├── __init__.py       # Initializes game-related modules
│   │   ├── engine.py         # Contains the GameEngine class for game logic
│   │   └── words.py          # Provides a list of words for the game
│   ├── ui
│   │   ├── __init__.py       # Initializes UI-related modules
│   │   ├── app.py            # Main application window class
│   │   └── components.py      # Defines UI components
│   └── services
│       └── state_manager.py   # Manages application state
├── tests
│   └── test_game.py          # Unit tests for game logic
├── requirements.txt           # Lists project dependencies
├── pyproject.toml            # Project configuration file
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd hangman-gui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python -m src.main
   ```

## Usage Guidelines

- Upon starting the application, players will be presented with a user-friendly interface to start the game.`
- Players can input their guesses through the provided input fields and will receive immediate feedback on their progress.
- The game tracks the number of incorrect guesses and displays the current state of the word being guessed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.