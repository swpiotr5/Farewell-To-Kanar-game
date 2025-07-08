# Farewell to Kanar

**Farewell to Kanar** is an arcade-style game written in Python using the Pygame library. Your goal is to escape from a bus before being caught by the ticket inspector (kanar). You must avoid the inspector's gaze, move between passengers, and reach the exit within the time limit!

## Gameplay

- You control a passenger trying to escape from the bus.
- The ticket inspector (kanar) periodically looks in your direction – if you are in his line of sight outside a safe zone, you get caught!
- The bus is filled with other passengers and obstacles you must avoid.
- Reach the green exit zone before the timer (60 seconds) runs out.
- You can hide in special safe zones where the inspector cannot see you.

## Controls

- **W** – move up
- **S** – move down
- **A** – move left
- **D** – move right
- **Space** – start the game from the main menu
- **Q** – quit the game
- **ESC** – exit after losing

## How to Run

1. Make sure you have Python 3.10+ and the `pygame` library installed:
   ```sh
   pip install pygame
   ```
2. Start the game with:
   ```sh
   python main.py
   ```

## Project Structure

- `main.py` – main menu and game launcher.
- [`Game.py`](Game.py) – core game logic, event handling, drawing, win/lose conditions.
- [`Person.py`](Person.py) – player (passenger) class.
- [`TicketController.py`](TicketController.py) – ticket inspector logic, vision and detection.
- [`LookFrontStrategy.py`](LookFrontStrategy.py), [`LookSideStrategy.py`](LookSideStrategy.py) – inspector's looking strategies.
- [`SafeZone.py`](SafeZone.py) – safe zones where the player is invisible to the inspector.
- [`Passenger.py`](Passenger.py), [`PassengersFactory.py`](PassengersFactory.py), [`PassengerZone.py`](PassengerZone.py) – passengers and their placement.
- [`Rectangle.py`](Rectangle.py), [`RectangleFactory.py`](RectangleFactory.py) – obstacles and their generation.
- [`Goal.py`](Goal.py) – the bus exit (goal).
- `assets/` – game graphics (backgrounds, characters, inspector, passengers).

## Game Mechanics

- The inspector randomly changes his looking direction using [`LookFrontStrategy`](LookFrontStrategy.py) and [`LookSideStrategy`](LookSideStrategy.py).
- If the player is in the inspector's line of sight and not in a [`SafeZone`](SafeZone.py), the game is lost.
- The player cannot pass through obstacles or other passengers.
- The game ends with a win if you reach the exit, or a loss if time runs out or you are caught.

## Authors

Project created for academic purposes.

---

Good luck escaping the inspector!
