"""
This is my CS50P final project. 

    It is an interactive game using pygame.
    Press space to jump, and don't collide with "haters"!

    INFO:

        Final Project Name: Bunny Hop
        Name: Selena Marwaha
        Location: Dubai, UAE
        Submission Date: October 15, 2025

        Github Username: codingmastermind514
        edX Username: s_marwaha
"""

# imports
import pygame
import random

"""
=======================
       CONSTANTS
=======================
"""
# sizes
GROUND_HEIGHT = 300
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SKY_HEIGHT = SCREEN_HEIGHT-GROUND_HEIGHT

# game  
GRND_SPEED = 10 * 60
SKY_SPEED = 1 * 60
ENEMY_TIME = 180

# bunny 
BUNNY_INIT_Y = GROUND_HEIGHT + 20
BUNNY_INIT_X = 30 
SPRITE_WIDTH = 150
SPRITE_HEIGHT = 160
HATER_HEIGHT = 100
HATER_WIDTH = 100
HATER_Y = BUNNY_INIT_Y + SPRITE_HEIGHT - HATER_HEIGHT

# physics 
GRAVITY = 0.45 * (60**2)
INIT_JUMP_SPEED = -14 * 60

# hater speeds
SLIME_SPEED = 18 * 60
ALIEN_SPEED = 13 * 60
MALAN_SPEED = 11 * 60

"""
=======================
      FUNCTIONS
=======================
"""
# font changer
fancy_letters = {
    'A': '𝒜', 'B': '𝐵', 'C': '𝒞', 'D': '𝒟', 'E': '𝐸', 'F': '𝐹', 'G': '𝒢',
    'H': '𝐻', 'I': '𝐼', 'J': '𝒥', 'K': '𝒦', 'L': '𝐿', 'M': '𝑀', 'N': '𝒩',
    'O': '', 'P': '𝒫', 'Q': '𝒬', 'R': '𝑅', 'S': '𝒮', 'T': '𝒯', 'U': '𝒰',
    'V': '𝒱', 'W': '𝒲', 'X': '𝒳', 'Y': '𝒴', 'Z': '𝒵',

    'a': '𝒶', 'b': '𝒷', 'c': '𝒸', 'd': '𝒹', 'e': '𝑒', 'f': '𝒻', 'g': '𝑔',
    'h': '𝒽', 'i': '𝒾', 'j': '𝒿', 'k': '𝓀', 'l': '𝓁', 'm': '𝓂', 'n': '𝓃',
    'o': '', 'p': '𝓅', 'q': '𝓆', 'r': '𝓇', 's': '𝓈', 't': '𝓉', 'u': '𝓊',
    'v': '𝓋', 'w': '𝓌', 'x': '𝓍', 'y': '𝓎', 'z': '𝓏',

    '!': '❣', '.': '.', '?': '¿', ':': ':',
    '1': '𝟣', '2': '𝟤', '3': '𝟥', '4': '𝟦', '5': '𝟧',
    '6': '𝟨', '7': '𝟩', '8': '𝟪', '9': '𝟫'
}

# chooses emoji for fancy_font
def choose_emoji(o):
    # list of 'o' emojis
    os = [
        '🍬', '🌞', '🐣', '🍡', '🥚', '🧁', '🍩',
        '🐼', '🍪', '🥝', '🌕', '🎈',  '🥥', '🍑'
    ]
    
    # return new o
    if o:
        return random.choice(os)

# font changer
def fancy_font(phrase):
    result = ""
    # replace using dict 
    for char in phrase: 
        # use emojis for all "o"s
        if char.lower() == 'o':
            result += choose_emoji(True)
        elif char in list(fancy_letters.keys()): 
            result += fancy_letters[char]
        else:
            result += char 

    return result

# TESTED: LOAD IMAGE
def load_image(path, dim):
    # loads image, converts alpha, resizes
    try:
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, dim)
        return image
    # error
    except FileNotFoundError:
        raise FileNotFoundError(f"Resource missing. {path} not found.")

# TESTED: CAP THE DT AT 50MS MAX
def cap_dt(dt, max_ms=50):
    return max_ms /1000 if dt > max_ms / 1000 else dt
    
# get dt and use cap_dt to max out just in case of delays / skips 
def get_dt(clock, max_ms=50, fps=60):
    dt = cap_dt(clock.tick(fps) / 1000)
    return dt 

# TESTED: update pos for bkgnd 
def scroll(pos, speed, width, dt):
    # background scroll & wraps over at boundary
    pos -= speed*dt
    if pos <= -width:
        pos = 0
    return pos

# display and calculate score
def display_score(score, screen):
    X = 300 # x pos
    Y = 200 # y pos

    # putting font and displaying
    font = pygame.font.Font('./resources/BoldPixels.ttf', 32) 
    text = font.render(f"Score: {int(score)}", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    # blit to screen
    screen.blit(text, textRect)
    
"""
=======================
        IMAGES
=======================
"""

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(fancy_font("Bunny Hop")) 

# sprites
bunny = load_image("./img/bunny.png", (SPRITE_WIDTH, SPRITE_HEIGHT))
deadbunny = load_image("./img/dead.png", (SPRITE_WIDTH, SPRITE_HEIGHT))
ambulance = load_image("./img/ambulance.png", (SPRITE_WIDTH, SPRITE_HEIGHT))

# background content    
sky = load_image("./img/background/sky.png", (SCREEN_WIDTH,SKY_HEIGHT))
clouds = load_image("./img/background/clouds.png", (SCREEN_WIDTH, SKY_HEIGHT))
ground = load_image("./img/background/grnd.png", (SCREEN_WIDTH, GROUND_HEIGHT))
gameover = pygame.image.load("./img/background/gameover.png")
again = pygame.image.load("./img/background/again.png")

# haters 
alien = load_image("./img/haters/alien.png", (SPRITE_WIDTH, SPRITE_HEIGHT))
slime = load_image("./img/haters/slime.png", (HATER_WIDTH, HATER_HEIGHT))
malan = load_image("./img/haters/malan.png", (HATER_WIDTH, HATER_HEIGHT))


"""
==========================
      CLASS: HATER
========================== 
"""

class Hater:
    """
    Class Name: Hater 

    Attributes: x, y, hater (hater_type)

    Methods: 
        draw_hater: draws the hater at a given position 
        move_hater: updates the hater's position based on speed 
        choose_hater: chooses a hater type randomly 
        rect: creates a 'rect' object for the hater
    """

    # attributes: hater type, x pos, y pos 
    def __init__(self):
        self.x = SCREEN_WIDTH # x
        self.y = HATER_Y # y
        self.hater = self.choose_hater() # current hater
        
    # draw the hater @ the position 
    def draw_hater(self, screen):
        screen.blit(self.hater["img"], (int(self.x), int(self.y))) # blit the hater

    # move the hater -> the screen
    def move_hater(self, dt):
        self.x -= self.hater["speed"] * dt # move the hater @ the speed specified

    # choose hater randomly
    def choose_hater(self):

        # Slime: 63% and fast
        # Prof. Galactico: 25% and mid speed
        # David J Malan: 12% and slow

        weights = [0.63, 0.25, 0.12]
        haters = [
            {
                "img":slime,
                "speed":SLIME_SPEED
            },
            {
                "img":alien,
                "speed":ALIEN_SPEED
            },
            {
                "img":malan,
                "speed":MALAN_SPEED
            }
        
        ]
        return random.choices(haters, weights = weights, k=1)[0] # return hater

    # hater rect 4 collision detection
    def rect(self):
        return pygame.Rect(self.x, self.y, HATER_WIDTH, HATER_HEIGHT) # rect w/ same dimensions as hater

"""
=======================
        MAIN
=======================
"""
def main():
    
    """
    =======================
          VARIABLES
    =======================
    """
    # position vars 
    bunny_speed_y = 0 
    bunny_y = BUNNY_INIT_Y
    on_ground = True

    hater_timer = 0 
    hater_spawn_delay = 0

    scroll_grnd = 0
    scroll_sky = 0 
    dead = False
    score = 0

    current_haters = []


    """
    =======================
           GAME LOOP
    =======================
    """
    running = True
    while running:
        
        #  if you X out of the tab, make sure this loop stops and the game quits 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # get dt and update score 
        dt = get_dt(clock)
        score += dt

        # if still alive... 
        if dead == False:
            
            # update position for bkgnd scrolling 
            scroll_grnd = scroll(scroll_grnd, GRND_SPEED, SCREEN_WIDTH, dt)
            scroll_sky = scroll(scroll_sky, SKY_SPEED, SCREEN_WIDTH, dt)
                
            # DISPLAY scrolling background 
            for i in range(2):
                screen.blit(ground, (scroll_grnd + i*SCREEN_WIDTH, SCREEN_HEIGHT-GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
                screen.blit(sky, (scroll_sky + i*SCREEN_WIDTH, 0, SCREEN_WIDTH, SKY_HEIGHT))
                screen.blit(clouds, (scroll_sky + i*SCREEN_WIDTH, 0, SCREEN_WIDTH, SKY_HEIGHT))
            
            # update and draw bunny + get rect for collision
            bunny_rect = pygame.Rect(BUNNY_INIT_X, bunny_y, SPRITE_WIDTH, SPRITE_HEIGHT)
            screen.blit(bunny, (BUNNY_INIT_X, int(bunny_y)))
                
            # bunny physics for jupming
            bunny_speed_y += GRAVITY * dt
            bunny_y += bunny_speed_y * dt

            # jump detection 
            if on_ground == True:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    bunny_speed_y = INIT_JUMP_SPEED
                    on_ground = False

            # prevents the bunny from falling into the infinite abyss 
            if bunny_y > BUNNY_INIT_Y:
                bunny_y = BUNNY_INIT_Y
                on_ground = True    

            # updating and drawing the haters every frame 
            hater_timer += dt
            if hater_timer >= hater_spawn_delay:
                current_haters.append(Hater())
                hater_timer = 0
                hater_spawn_delay = random.choice(range(3,5))

            # update haters and check for collision 
            # if you collide... DEATH AND DESTRUCTION! 
            for hater in current_haters:
                hater.move_hater(dt)
                hater.draw_hater(screen)
                hater_rect = hater.rect() 
                if hater_rect.colliderect(bunny_rect):
                    dead = True

            # remove off-screen haters 
            current_haters = [hater for hater in current_haters if hater.x >= -100]
            
            # display current score
            display_score(score, screen)
        
        # if dead... 
        else:
            # draw a flat, non-moving background 
            screen.blit(ground, (0, SCREEN_HEIGHT-GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
            screen.blit(sky, (0, 0, SCREEN_WIDTH, SKY_HEIGHT))
            screen.blit(clouds, (0, 0, SCREEN_WIDTH, SKY_HEIGHT))
            
            # draw the bunny and ambulance in the middle of the screen
            screen.blit(deadbunny, (520, HATER_Y))
            screen.blit(ambulance, (690, HATER_Y))

            # enter to re-play
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                main()

            # show game-over and play again messages / images
            screen.blit(gameover, (140, 100))
            screen.blit(again, (140, 250))

        # put all this on screen
        pygame.display.flip() 

# run main
if __name__ == "__main__":
    main()