#paddle_ball_game

A detailed README for a simple game built with **Pygame**. This file explains the project step by step — how to run it, requirements, code explanation, improvement suggestions, and common troubleshooting.

---

## Overview

A simple game: a ball falls from the top and a paddle moves with the mouse. If the ball touches the paddle, the score increases, and the ball resets to the top at a random position. If the ball reaches the bottom, the game ends and can be restarted by clicking the mouse.

This game works well as a learning project or a small demo.

---

## Project Structure (Suggested)

```
ball-game/
├── README.md               # This file
├── game.py                 # Main code file (or main.py)
├── requirements.txt        # Dependencies (example: pygame)
├── assets/                 # Folder for sounds/images if any
│   ├── hit.wav
│   └── background.png
└── LICENSE
```

---

## Requirements

* Python 3.7 or newer (3.8+ recommended)
* Pygame library

Install Pygame:

```bash
pip install pygame
```

It’s best to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate     # Windows
pip install pygame
```

---

## How to Run

Save the code in a file like `game.py` and run it:

```bash
python game.py
```

Make sure you are on a system with a graphical interface (not a headless server). Otherwise, you’ll get the error "No available video device."

---

## Game Controls

* Move the mouse left/right to move the paddle.
* On the `Game Over` screen, left-click to restart.
* Close the window to exit the game.

---

## Code Explanation (Detailed)

The main code is divided into clear sections — here’s what each part does:

### 1) Initialization

* `pygame.init()` : initialize Pygame.
* `screen = pygame.display.set_mode((600,600))` : open a 600x600 window.
* `pygame.display.set_caption("Ball Game")` : set the window title.
* `clock = pygame.time.Clock()` : create a clock to control FPS.

### 2) Core Variables

* `running` : flag to control the main loop.
* `x` : paddle x-coordinate (paddle stays fixed vertically).
* `xc, yc` : ball coordinates.
* `score` : score counter.
* `gameover` : flag for game state.
* `font` : for rendering text (score and Game Over).

### 3) Main Game Loop

* `for event in pygame.event.get():` : read system events (quit, etc.).
* Fill background `screen.fill((255,0,0))` to make it red.

### 4) Gameplay Logic (when not over)

* Move ball down: `yc = yc + 3` (adjust value to change speed).
* Draw ball: `h = pygame.draw.circle(screen, (255,255,255), (xc, yc), 10)` — note: `draw.circle` returns a Rect.
* Get mouse x-position: `x = pygame.mouse.get_pos()[0]`, then draw paddle `d = pygame.draw.rect(..., (x,500,200,50))`.
* Collision detection: `if h.colliderect(d):`

  * Increase score: `score += 1`
  * Reset ball to top: `yc = 0`
  * Randomize x-position: `xc = random.randint(0,500)`
* Render score using `font.render("Score: " + str(score), True, (255,255,255))`.
* If `yc > 550` → set `gameover = True`.

### 5) Game Over Screen

* Show "Game Over" text.
* Restart when left mouse button is clicked: reset `gameover=False, score=0, yc=0`.

### Current Limitations

* Paddle is not restricted to screen bounds.
* Ball speed is fixed.
* Score resets to 0 after restart (no highscore saving).

---

## Improvement Suggestions (with Examples)

1. **Keep paddle inside screen bounds**:

```python
paddle_width = 200
mouse_x = pygame.mouse.get_pos()[0]
x = max(0, min(mouse_x - paddle_width//2, 600 - paddle_width))
```

2. **Increase difficulty over time**:

```python
speed = 3
speed += 0.01
yc += speed
```

3. **Save high score to a file**:

```python
try:
    with open('highscore.txt','r') as f:
        highscore = int(f.read().strip() or 0)
except FileNotFoundError:
    highscore = 0

if score > highscore:
    highscore = score
    with open('highscore.txt','w') as f:
        f.write(str(highscore))
```

4. **Add sound effects**:

```python
pygame.mixer.init()
hit_sound = pygame.mixer.Sound('assets/hit.wav')
hit_sound.play()
```

5. **Refactor into functions** (`init_game()`, `reset_ball()`, `draw()`, `update()`) for readability.

6. **Add a main menu** with a Start button and controls info.

---

## Improved Example Code

```python
import pygame, random

def reset_ball():
    return random.randint(10, 590), 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,36)

    xc, yc = reset_ball()
    score = 0
    speed = 3
    paddle_w = 200
    gameover = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255,0,0))

        if not gameover:
            yc += speed
            ball_rect = pygame.draw.circle(screen,(255,255,255),(xc,yc),10)
            mouse_x = pygame.mouse.get_pos()[0]
            paddle_x = max(0, min(mouse_x - paddle_w//2, 600 - paddle_w))
            paddle_rect = pygame.draw.rect(screen,(255,255,255),(paddle_x,500,paddle_w,50))

            if ball_rect.colliderect(paddle_rect):
                score += 1
                xc, yc = reset_ball()

            txt = font.render(f"Score: {score}", True, (255,255,255))
            screen.blit(txt,(10,10))

            if yc > 550:
                gameover = True
        else:
            txt = font.render("Game Over", True, (255,255,255))
            screen.blit(txt,(200,300))
            if pygame.mouse.get_pressed()[0]:
                gameover = False
                score = 0
                xc, yc = reset_ball()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
```

---

## Common Issues & Fixes

* **ModuleNotFoundError: No module named 'pygame'**

  * Fix: install pygame (`pip install pygame`) or activate your virtualenv.

* **OSError: No available video device**

  * Happens on headless servers. Fix: run on a local machine or use Xvfb.

* **Window too small / paddle off-screen**

  * Fix: ensure paddle\_x is clamped within screen bounds.
