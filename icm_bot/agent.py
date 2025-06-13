import pyautogui

class Agent:
    """Handle direct interactions with the UI such as mouse movements and clicks."""

    def click(self, x: int | None = None, y: int | None = None) -> None:
        """Click at the given position or at the current mouse position."""
        if x is not None and y is not None:
            pyautogui.click(x, y)
        else:
            pyautogui.click()

    def move_to(self, x: int, y: int) -> None:
        """Move the mouse to the given coordinates."""
        pyautogui.moveTo(x, y)
