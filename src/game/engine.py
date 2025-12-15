import random
from src.game.words import escolher_palavra

class GameEngine:
    def __init__(self):
        self.secret_word = None
        self.guesses = set()
        self.max_attempts = 6
        self.attempts = 0
        self.game_over = False

    def start_new_game(self):
        self.secret_word = escolher_palavra()
        self.guesses = set()
        self.attempts = 0
        self.game_over = False

    def make_guess(self, letter):
        if self.game_over:
            raise Exception("Game is already over. Please reset the game to play again.")
        
        letter = letter.upper()
        if letter in self.guesses:
            return False  # Letter has already been guessed

        self.guesses.add(letter)

        if letter not in self.secret_word:
            self.attempts += 1

        if self.attempts >= self.max_attempts:
            self.game_over = True

        return True

    def get_display_word(self):
        if not self.secret_word:
            return ""
        return ' '.join(letter if letter in self.guesses else '_' for letter in self.secret_word)

    def is_winner(self):
        if not self.secret_word:
            return False
        return set(self.secret_word).issubset(self.guesses)

    def is_loser(self):
        return self.attempts >= self.max_attempts
    
    def get_status(self):
        return f"Tentativas restantes: {self.get_remaining_attempts()}"
    
    @property
    def current_word(self):
        return self.secret_word

    def get_remaining_attempts(self):
        return self.max_attempts - self.attempts

    def get_secret_word(self):
        return self.secret_word if self.game_over else None