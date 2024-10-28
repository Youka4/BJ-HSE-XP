
import tkinter as tk
from gui.game_screen import GameScreen
from gui.gui_manager import GUIManager


def main():
    root = tk.Tk()
    root.geometry("600x400")
    GUIManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
