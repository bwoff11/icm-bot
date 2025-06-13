from __future__ import annotations

import threading
from pynput import keyboard

from .agent import Agent
from .ui import BotUI


class BotController:
    def __init__(self):
        self.active = False
        self.agent = Agent()

    def toggle_active(self):
        self.active = not self.active
        state = "activated" if self.active else "deactivated"
        print(f"Bot {state}")

    def is_active(self) -> bool:
        return self.active


def main() -> None:
    controller = BotController()

    def on_activate():
        controller.toggle_active()

    hotkeys = keyboard.GlobalHotKeys({"<f1>": on_activate})
    hotkeys.start()

    ui = BotUI(controller.is_active)
    try:
        ui.run()
    finally:
        hotkeys.stop()


if __name__ == "__main__":
    main()
