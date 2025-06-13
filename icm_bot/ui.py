import tkinter as tk
import pyautogui


class BotUI:
    """Basic window displaying bot state and mouse coordinates."""

    def __init__(self, get_state):
        self.get_state = get_state
        self.root = tk.Tk()
        self.root.title("ICM Bot")

        self.name_label = tk.Label(self.root, text="Idle Cave Miner Bot")
        self.name_label.pack(pady=4)

        self.coord_var = tk.StringVar()
        self.coord_label = tk.Label(self.root, textvariable=self.coord_var)
        self.coord_label.pack(pady=4)

        self.state_var = tk.StringVar()
        self.state_label = tk.Label(self.root, textvariable=self.state_var)
        self.state_label.pack(pady=4)

        self.update_labels()

    def update_labels(self):
        x, y = pyautogui.position()
        self.coord_var.set(f"Mouse: {x}, {y}")
        self.state_var.set("Active" if self.get_state() else "Inactive")
        self.root.after(100, self.update_labels)

    def run(self):
        self.root.mainloop()
