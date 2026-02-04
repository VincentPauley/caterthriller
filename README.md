# Caterthriller

Thrilling arcade game where you are a caterpillar.

## Technologies

- Pygame

## Development Setup

### Prerequisites
- Python 3.9 or higher

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd caterthriller
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
```

3. Activate the virtual environment:
- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```
- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```

4. Install dependencies:
```bash
pip install pygame
```

5. Run the game (from root directory):
```bash
python src/main.py
```

### Deactivating the Virtual Environment
When you're done working, deactivate the virtual environment:
```bash
deactivate
```

## Movement

Precise and nimble movement is a huge requirement of the game.  Right now side to side accel is in place but want to adjust
so that once fingers are off the keyes for .2 seconds (or whatever) that the player is "shifted" to the center of the lane
that they are moving toward (or closest to etc) - gonna need a bit of tuning and tweaking.

Start by creating spaces on the center of each centerx of a lane