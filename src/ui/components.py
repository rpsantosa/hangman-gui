import tkinter as tk
from tkinter import messagebox

class HangmanButton(tk.Button):
    def __init__(self, master, letter, command=None):
        super().__init__(master, text=letter, command=command)
        self.letter = letter

class HangmanLabel(tk.Label):
    def __init__(self, master, text):
        super().__init__(master, text=text, font=("Helvetica", 24))

class HangmanEntry(tk.Entry):
    def __init__(self, master):
        super().__init__(master, font=("Helvetica", 24), width=2)
        self.config(justify='center')

class HangmanFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

    def add_button(self, letter, command):
        button = HangmanButton(self, letter, command)
        button.pack(side=tk.LEFT)

    def add_label(self, text):
        label = HangmanLabel(self, text)
        label.pack()

    def add_entry(self):
        entry = HangmanEntry(self)
        entry.pack()

class GameComponents:
    def __init__(self, root, game_engine):
        self.root = root
        self.game_engine = game_engine
        self.word_label = None
        self.status_label = None
        self.input_entry = None
    
    def create_title(self):
        title = tk.Label(self.root, text="Jogo da Forca", font=("Helvetica", 32, "bold"))
        title.pack(pady=20)
    
    def create_word_display(self):
        self.word_label = tk.Label(self.root, text="_ _ _ _", font=("Helvetica", 36))
        self.word_label.pack(pady=20)
    
    def create_input_field(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Digite uma letra:", font=("Helvetica", 14)).pack(side=tk.LEFT, padx=5)
        self.input_entry = tk.Entry(input_frame, font=("Helvetica", 18), width=5)
        self.input_entry.pack(side=tk.LEFT, padx=5)
    
    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        guess_button = tk.Button(button_frame, text="Adivinhar", font=("Helvetica", 14), 
                                command=self.root.master.handle_guess if hasattr(self.root, 'master') else None)
        guess_button.pack(side=tk.LEFT, padx=10)
        
        new_game_button = tk.Button(button_frame, text="Novo Jogo", font=("Helvetica", 14),
                                    command=self.root.master.start_game if hasattr(self.root, 'master') else None)
        new_game_button.pack(side=tk.LEFT, padx=10)
    
    def create_status_display(self):
        self.status_label = tk.Label(self.root, text="Tentativas restantes: 6", font=("Helvetica", 16))
        self.status_label.pack(pady=10)
    
    def update_word_display(self, word):
        if self.word_label:
            self.word_label.config(text=word)
    
    def update_status_display(self, status):
        if self.status_label:
            self.status_label.config(text=status)
    
    def get_guess(self):
        if self.input_entry:
            guess = self.input_entry.get().strip().upper()
            self.input_entry.delete(0, tk.END)
            return guess
        return ""

def show_message(title, message):
    messagebox.showinfo(title, message)