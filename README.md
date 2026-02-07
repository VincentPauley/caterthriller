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

[ ] - player needs to be contained on the platform and bounce of the sides as needed

        - if speed over a certain threshold they go back to 0, 1, or 2 spaces etc. if a bounce is
          in effect it cannot be interrupted by input for the duration.

[ ] - player positioning/wall creep (should get 3 chances before being knocked back into spider)
[ ] - overhanging leaves at the top should move x slightly depending on player position, adds a layer
of interest and gives player clearest view in the middle.

Block Removal Next:

- include phases based on how far along user is...
  [X] - phase 1: 2 sequential blocks removed
  [X] - phase 2: 2 blocks removed, sequential not guaranteed
  [ ] - phase 3: 1 block removed, max of 5 movement
  [ ] - phase 4: 1 block removed, max of 5 movement, speed increase
  [ ] - phase 5: 1 block removed, long biased movement, speed remains high
  ... shifting back and forth blocks!
