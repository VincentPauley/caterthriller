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

## Todos

[ ] - wall_manager needs to emit a signal when the player passes a wall
[ ] - player needs to be contained on the platform and bounce of the sides as needed

        - if speed over a certain threshold they go back to 0, 1, or 2 spaces etc. if a bounce is
          in effect it cannot be interrupted by input for the duration.
