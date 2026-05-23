# MEOW RUNNER

Meow Runner is a cat-themed remake of the classic Chrome offline dinosaur game, developed as the final project for the Software Engineering course at UNIBO.

This 2D endless runner game was developed in Python using the Pygame library. Players control a cat, navigating through various obstacles to achieve the highest score.

## Features
- **Dynamic Difficulty:** The game speed increases as the player's score grows.
- **Multiple Obstacles:** Avoid plants, gorges and bees.
- **Visual Debug Mode:** Includes a built-in debug view to visualize hitboxes for development and testing.

## Prerequisites
- **Python 3.x** installed on your system.

## Project Setup
1. **Download the Project:** Clone this repository or download the source code as a ZIP file and extract it on your computer.
2. **Open Terminal:** Open your terminal or command prompt and navigate into the project's root folder.
3. **Install Dependencies:** Install the required packages using the installation code block provided below.
4. **Launch the Game:** Run the execution command to start playing Meow Runner!

## Code Commands
**Install Requirements**

Run this command to install the necessary game files directly onto your system:

```bash
pip install -r requirements.txt
```

**Game Launching**

Once the requirements are installed, use this command to start the game loop:

```bash
python main.py
```

**Running Tests**

To execute the automated unit and integration tests along with the code coverage tracking, run:

```bash
pytest --cov=source tests/
```

# Recommendation: 
**Virtual environment setup** 

If you prefer to keep your global Python system clean and avoid package version conflicts, you can set up a virtual environment before running the install steps above.

```bash
python -m venv venv
```
```bash
.\venv\Scripts\Activate.ps1
```
