# icm-bot

A simple bot framework for the *Idle Cave Miner* clicker game. The project is
split into two domains:

- **Agent** – handles low level interaction with the operating system (mouse
  clicks and movements).
- **UI** – shows a small window with the current mouse position and whether the
  bot is active.

Press **F1** at any time to toggle the bot on or off. The window updates as the
mouse moves so you can see the current coordinates.

## Running

Install the dependencies and run the bot:

```bash
pip install -r requirements.txt
python -m icm_bot.main
```

