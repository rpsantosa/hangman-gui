import tkinter as tk
from tkinter import messagebox
from src.game.engine import GameEngine
from src.ui.components import GameComponents

class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.game_engine = GameEngine()
        self.components = GameComponents(self.root, self.game_engine)
        self.root.master = self  # Allow components to call app methods
        self.setup_ui()

    def setup_ui(self):
        self.components.create_title()
        self.components.create_word_display()
        self.components.create_input_field()
        self.components.create_buttons()
        self.components.create_status_display()

    def start_game(self):
        self.game_engine.start_new_game()
        self.update_ui()

    def update_ui(self):
        self.components.update_word_display(self.game_engine.get_display_word())
        self.components.update_status_display(self.game_engine.get_status())

    def handle_guess(self):
        guess = self.components.get_guess()
        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Tentativa inválida", "Por favor, digite uma única letra.")
            return
        
        if self.game_engine.make_guess(guess):
            self.update_ui()
            if self.game_engine.is_winner():
                messagebox.showinfo("Parabéns!", "Você venceu!")
                self.start_game()
            elif self.game_engine.is_loser():
                messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra era: {self.game_engine.current_word}")
                self.start_game()
        else:
            messagebox.showwarning("Tentativa inválida", "Você já tentou essa letra.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()