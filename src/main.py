import tkinter as tk
from src.ui.app import HangmanApp

def main():
    root = tk.Tk()
    app = HangmanApp(root)
    app.start_game()
    root.mainloop()

if __name__ == "__main__":
    main()