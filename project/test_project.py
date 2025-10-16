"""
This is my CS50P final project test file.

    This tests 3 functions from project.py: load_image(), cap_dt(), and scroll()

    INFO:

        Final Project Name: Bunny Hop
        Name: Selena Marwaha
        Location: Dubai, UAE
        Submission Date: October 15, 2025

        Github Username: codingmastermind514
        edX Username: s_marwaha
"""
import pytest
from project import load_image, cap_dt, scroll
import pygame

def test_load_image():
    # check throws errors 
    with pytest.raises(FileNotFoundError):
        load_image("./img/bun.png", (100,100))
    
    with pytest.raises(FileNotFoundError):
        load_image("./img/ghoul.png", (100,100))
    
    with pytest.raises(FileNotFoundError):
        load_image("./img/peepeepoopoo.png", (100,100))
    
    # test bunny 
    bunny = pygame.image.load("./img/bunny.png").convert_alpha()
    bunny = pygame.transform.scale(bunny, (100,100))
    bunny_test = load_image("./img/bunny.png", (100,100))

    assert bunny_test.get_size() == bunny.get_size()
    assert pygame.image.tostring(bunny_test, "RGBA") == pygame.image.tostring(bunny, "RGBA")

    # test malan 
    malan = pygame.image.load("./img/haters/malan.png").convert_alpha()
    malan = pygame.transform.scale(malan, (100,100))
    malan_test = load_image("./img/haters/malan.png", (100,100))

    assert malan_test.get_size() == malan.get_size()
    assert pygame.image.tostring(malan_test, "RGBA") == pygame.image.tostring(malan, "RGBA")


"""
The cap_dt function is responsible for... 

    cap_dt(dt, max_ms=50)

We only call the cap_dt function with clock.tick(),
so no try-catch or errors raised as we cannot expect string input
"""
def test_cap_dt():
    # test with default arg
    assert cap_dt(.04) == .04
    assert cap_dt(.067) == .05

    # test with set max_ms 
    assert cap_dt(.04, max_ms=45) == .04
    assert cap_dt(.067, max_ms=45) == .045


"""
"""
def test_scroll():
    # past boundary 
    assert scroll(-1287, 3, 1280, 5) == 0

    # zero speed 
    assert scroll(-1279, 0, 1280, 5) == -1279
    
    # zero dt 
    assert scroll(-1279, 3, 1280, 0) == -1279

    # normal
    assert scroll(-1255, 3, 1280, 5) == -1270

    # @ boundary 
    assert scroll(-1265, 3, 1280, 5) == 0