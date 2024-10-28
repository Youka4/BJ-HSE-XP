
import tkinter as tk
from gui.game_screen import GameScreen

def main():
    root = tk.Tk()
    root.geometry("600x400")
    GameScreen(root, lambda: root.quit())
    root.mainloop()

if __name__ == "__main__":
    main()
