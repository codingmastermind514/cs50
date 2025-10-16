# Bunny H🍪p

## Overview
An overview of my project, Bunny H🍪p.\
*Disclaimer: This is in `pygame`. I was unable to play it on cs50.dev and developed it locally. If it doesn't work or doesn't support `pygame` please run it on a platform that supports `pygame` aka locally. I worked in a local environment in VS Code.*

&nbsp;&nbsp;&nbsp;&nbsp;**💡 Creator**: Selena Marwaha, Age 11

&nbsp;&nbsp;&nbsp;&nbsp;**💡 GitHub Username**: [`codingmastermind514`](https://github.com/codingmastermind514)

&nbsp;&nbsp;&nbsp;&nbsp;**💡 EdX Username**: `s_marwaha`

&nbsp;&nbsp;&nbsp;&nbsp;**💡 Video Demo**: [`CS50P Final Project`](https://www.youtube.com/watch?v=Ke9dhvjwoK8)

### Short Description:
Bunny H🍪p is a game where you make a character jump over obstacles. There is a score to display how far you get into the game based on time. Get as far as you can!

&nbsp;&nbsp;&nbsp;&nbsp;**💡 Character:** Bunny in car 🐰🚗

&nbsp;&nbsp;&nbsp;&nbsp;**💡 Obstacles:** Enemies are Professor Galactico 👽, David J Malan 👨‍💻 and a Slime Monster 👾

&nbsp;&nbsp;&nbsp;&nbsp;**💡 Goal:** To beat your score (to get farther into the game)

## Gameplay and Features

### Gameplay

**💡 How to Play 💡**

You, the bunny, are in your car, driving. Haters come to stop you at different speeds from the right side. If you collide with a hater, you die. To not die, you need to be able to get over the obstacles. To do THAT, you need to jump over them. To jump, you need to hit the `space bar`. Once you die, you will be directed to a **Game Over** screen. To play again, you hit the `enter` or `return` key.

**🐰 Scoring 🐰**

You get 'points' added to your score for each second that you play. One point is equal to one second of gameplay. Try to beat your high score!

### Features

#### Background

The ground and the sky scroll while the bunny *stays still* to make it *seem* like the bunny moves. The ground and the sky move at different speeds. I made it this way because thing that are closer to to you appear to move faster and things farther from you appear to move slower. If the ground and the sky were *not* moving at different speeds, the game would seem unnatural and less realistic.


```
# DISPLAY scrolling background
for i in range(2):
    screen.blit(ground, (scroll_grnd + i*SCREEN_WIDTH, SCREEN_HEIGHT-GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

    screen.blit(sky, (scroll_sky + i*SCREEN_WIDTH, 0, SCREEN_WIDTH, SKY_HEIGHT))

    screen.blit(clouds, (scroll_sky + i*SCREEN_WIDTH, 0, SCREEN_WIDTH, SKY_HEIGHT))
```

This code is the same as:

```
screen.blit(ground, (scroll_grnd, SCREEN_HEIGHT-GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
screen.blit(ground, (scroll_grnd + SCREEN_WIDTH, SCREEN_HEIGHT-GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

screen.blit(sky, (scroll_sky, 0, SCREEN_WIDTH, SKY_HEIGHT))
screen.blit(sky, (scroll_sky + SCREEN_WIDTH, 0, SCREEN_WIDTH, SKY_HEIGHT))

screen.blit(clouds, (scroll_sky, 0, SCREEN_WIDTH, SKY_HEIGHT))
screen.blit(clouds, (scroll_sky + SCREEN_WIDTH, 0, SCREEN_WIDTH, SKY_HEIGHT))
```

This code draws *two images* because if there was only one, the background would basically scroll into the endless void of space (as in go off the screen never to return). Since this `for` loop is in the game loop, the background gets redrawn every iteration of the loop which is around 60 times a second.

The `scroll_sky` and `scroll_grnd` variables are updated using the `scroll()` funtion. These variables represent horizontal position (x coordinate) of the image.

#### Haters
Haters are essentialy *enemies*  in my game and if you collide with them, you die 😵.

There are 3 types of haters. Each type has a different speed, appearance, and spawn rate. The types are:

**Common (63%):** Slime Monster \
*Note: The slime monster is the fastest hater even though it is the most common.*

**Rare' (25%):** Professor Galactico \
*Note: Many thanks to François Taddei for introducing me to Professor Galactico.*

**ULTRA Rare (12%):** David J Malan \
*Note: David J Malan is the slowest hater.* \
*Double note: Including him in my game was done with much respect.*


## Setup
I used two libraries in this project.

**🎮 `pygame` 🎮** \
I used `pygame` to build my entire game! This library is made for making games, so it was the perfect choice.

**🎲 `random` 🎲** \
I used `random` in three different ways.

- *Hater Types*

    I used it to randomly (but in a biased way because I added weights) choose the type of hater to spawn (slime, Prof. Galactico, or David J Malan).

- *Hater Spawn Timing*

    I used it to randomise the hater spawn delay between 3 and 4 seconds. This makes sure that haters do not spawn at regular intervals, which makes the game more difficult and fun.

- *Fancy Font*

    I used it to choose an emoji for the `choose_emoji` function to randomise which emoji the 'o' in Bunny Hop appears e.g (instead of Bunny Hop, Bunny H🍩p). This is used in `fancy_font` which converts the caption into fancy letters because the `pygame.display.set_caption` function cannot handle such characters.


## Structure
The structure of my project is:

```
project/
├── README.md
├── project.py
├── test_project.py
├── requirements.txt
├── img/
│ └── bunny.png
| └── dead.png
| └── ambulance.png
| └── haters/
|   └── alien.png
|   └── malan.png
|   └── slime.png
| └── background/
|   └── again.png
|   └── gameover.png
|   └── sky.png
|   └── clouds.png
|   └── grnd.png
├── resources/
│ └── BoldPixels.ttf
└──
```

The folders are:

- *`project/`*:

    Main folder in which all project files and assets are contained.

- *`img/`*:

    Folder that contains all images, incuding background, main character, game over, etc.

- *`img/haters/`*:

    Contains images of haters, a.k.a. prof. galactico, the slime, and David J Malan's head.

- *`img/background/`*:

    Contains images of the background, including sky, clouds, and ground.

- *`resources/`*:

    Contains the font file in a `.ttf` format for the score.

The files are:

- *`project.py`*:

    The main `pygame` project including all functions and classes.

- *`test_project.py`*:

    3 functions that collectively test the implementations of `scroll`, `cap_dt` and `load_image` using `pytest`.

- *`requirements.txt`*:

    Any `pip`-installable libraries used in `project.py`, one per line.

- *`README.md`*:

    A brief overview of my Final Project!!!!

The assets are:

- *Images*

    All images are in `project/img`. Images are the background (sky, clouds, ground), haters (Prof. Galactico, David J Malan, slime), characters (bunny, bunny crashed, ambulance), and system messages (game over, play again).

- *Fonts*

    The font is called Bold Pixels, and it is in the resources folder with the `.ttf` extension. It is used for applying the font to the score displayed throughout the game.

## Architecture

### Functions
The first of my testable functions is `cap_dt`. It is used to cap the delta time (the time between frames) in the game so it doesn't get all janky.

```
def cap_dt(dt, max_ms=50):
    return max_ms/1000 if dt > max_ms/1000 else dt
```

The `scroll` function is used to do the background scroll. The position resets if the first image is fully off the screen.

```
def scroll(pos, speed, width, dt):
    pos -= speed*dt
    if pos <= -width:
        pos = 0
    return pos
```


### Classes
The `Hater` class is responsible for a good part of the game's logic, as seen below.

```
class Hater:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = HATER_Y
        self.hater = self.choose_hater()

    def draw_hater(self, screen):
        ...

    def move_hater(self, dt):
        ...

    def choose_hater(self):
        ...

    def rect(self):
        ...
```

The hater class has several methods.

- *`draw_hater(self, screen)`*

    This method is used to draw the hater. I call it when I have to spawn haters. It uses the `screen` to blit the hater at its current `x` and `y` position.


- *`move_hater(self, dt)`*

    This method is used to move the hater, or update its position. The hater's position is updated every frame based on its speed.


- *`choose_hater(self)`*

    This method is used to chose the hater randomly. This is only used internally. When a user makes a new hater, I call it to choose the type in the constructor.

- *`rect(self)`*

    This method is used to make a rectangle for the hater. This is necessary to use `pygame`'s collision detection. I make a rectangle in the same position and the same size as the hater itself.


### Logic
Lots of the game logic occurs within the game loop. The background scrolling has already been explained above. A few other important snippets of code are included below.

First, the physics. The bunny's movement is controlled using basic physics, as seen below. This allows it to jump. It is important to make sure the bunny doesn't jump once then fall infinitely. To do so, we have `on_ground`, which says whether the bunny is on the ground or not.

```
# bunny physics
bunny_speed_y += GRAVITY * dt
bunny_y += bunny_speed_y * dt

# jumping
if on_ground == True:
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        bunny_speed_y = INIT_JUMP_SPEED
        on_ground = False

# dont let the bunny fall into the infinite abyss!
if bunny_y > BUNNY_INIT_Y:
    bunny_y = BUNNY_INIT_Y
    on_ground = True
```

Next, delta time, or `dt`. I used `dt` because the game started to slow down A LOT. Instead of saying, "Let's have 60 frames per second," I use `dt` to update the movement based on how much time it takes for each frame rather than how many frames I think there should be per second. When the computer slows down, the motion looks normal.

```
# get dt and use cap_dt to max out just in case of delays / skips
def get_dt(clock, max_ms=50, fps=60):
    dt = cap_dt(clock.tick(fps) / 1000)
    return dt

dt = get_dt(clock)
```

Next, hater spawning. Haters are spawned randomly between 3 to 4 seconds. Haters are removed when they go off the screen using list comprehension.

```
# spawn a hater
hater_timer += dt
if hater_timer >= hater_spawn_delay:
    current_haters.append(Hater())
    hater_timer = 0
    hater_spawn_delay = random.choice(range(3,5))

# remove off-screen haters
current_haters = [hater for hater in current_haters if hater.x >= -100]
```

Lastly, collision. If the bunny and the hater collide,  you die. For this, I use `pygame`'s `Rect.colliderect(Rect)` function. This triggers a **Game Over** screen to be displayed.

```
# update and draw haters and check for collision
for hater in current_haters:
    hater.move_hater(dt)
    hater.draw_hater(screen)
    hater_rect = hater.rect()

    # check for collision!
    if hater_rect.colliderect(bunny_rect):
        dead = True
```

## Next Steps
If I had more time, I would implement the following features.

- *Levels*

    Increased difficulties as you work through the levels.

- *Prizes*

    These give you a boost and you hit them to collect them.

- *Bunny Customizer*

    Somewhere you can customize the colors and such of the bunny.

Maybe once CS50 ends!

## Acknowledgements
Thank you to the following people for supporting my CS50P journey:

- Thanks to Bella Tarantino for mentoring me.

- Also thanks to my mom who helped me when things got tough

- And lastly thanks to David J Malan who taught me everything I know now.

    P.S. I love your lectures!!!

My images and assets came from:

- **Sky, clouds, and ground:** Generated by OpenAI's [ChatGPT](http://chatgpt.com/)

- **Bunny, dead bunny, and slime:** Drawn by me on [Pixilart](https://www.pixilart.com)

- **Ambulance:** Found on [Shutterstock](https://www.shutterstock.com/image-vector/ambulance-car-icon-pixel-art-2547154963?dd_referrer=https%3A%2F%2Fwww.google.com%2F)

- **Font:** BoldPixels by Yuki Pixels on [1001fonts](https://www.1001fonts.com/boldpixels-font.html)

- **David J Malan:** Found on [WikiPedia](https://en.wikipedia.org/wiki/David_J._Malan) and edited on [Canva](https://www.canva.com/)

- **Prof. Galactico:** A photo taken by François Taddei, founder of [Learning Planet Institute in Paris](https://www.learningplanetinstitute.org/en/)
