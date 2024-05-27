import time
import hzckUtil
import FileUtil as fu
import machine
from BNST7735Driver import BNST7735Driver, BNColor
from BN165DKBDriver import keyCode
from machine import Pin

# ST7735 Init
bnsd = BNST7735Driver(4, 48, 5, 2)

# KeyPad Init
CP = Pin(41, Pin.OUT)
CE = Pin(39, Pin.OUT)
PL = Pin(40, Pin.OUT)
Q7 = Pin(21, Pin.IN)
adcIn = (CP, CE, PL, Q7)

black = BNColor(0, 0, 0)
dark_green = BNColor(0, 128, 0)
light_green = BNColor(0, 255, 0)

options = [
    ("Start", 20, 40),
    ("Ranking", 20, 60),
    ("Mistakes", 20, 80),
    ("User-Manage", 20, 100)
]

def display_opt(highlight):
    """
    Display the menu options on the screen with the highlighted option.

    Args:
    highlight (int): Index of the option to highlight.
    """
    bnsd.clear(black)
    bnsd.drawText("Greeting!", dark_green, 20, 10)
    for index, (text, x, y) in enumerate(options):
        color = light_green if index == highlight else dark_green
        bnsd.drawText(text, color, x, y)
    bnsd.show()

def update_highlight(highlight, kc):
    """
    Update the highlighted option based on key code input.

    Args:
    highlight (int): Current highlight index.
    kc (int): Key code input.

    Returns:
    int: Updated highlight index.
    """
    if kc == 2:
        highlight = (highlight + 1) % len(options)
    elif kc == 0:
        highlight = (highlight - 1) % len(options)
    elif kc == 6:
        if highlight == 0:
            df()
        elif highlight == 1:
            rk()
        elif highlight == 2:
            ms()
        elif highlight == 3:
            us()

    return highlight

def start(highlight=0):
    """
    Start the main loop to display and navigate menu options.

    Args:
    highlight (int): Starting highlight index, default is 0.
    """
    while True:
        kc = keyCode(adcIn)

        highlight = update_highlight(highlight, kc)
        display_opt(highlight)

        time.sleep(0.2)

def st():
    """
    Display "Under Development" message and wait for a specific key input to break the loop.
    """
    while True:
        kc = keyCode(adcIn)
        bnsd.clear(black)
        bnsd.drawText("Under", light_green, 30, 40)
        bnsd.drawText("Development", light_green, 30, 60)
        bnsd.show()
        if kc == 7:
            break
        time.sleep(0.1)

def rk():
    """
    Display "Under Development" message and wait for a specific key input to break the loop.
    """
    while True:
        kc = keyCode(adcIn)
        bnsd.clear(black)
        bnsd.drawText("Under", light_green, 30, 40)
        bnsd.drawText("Development", light_green, 30, 60)
        bnsd.show()
        if kc == 7:
            break
        time.sleep(0.1)

def ms():
    """
    Display "Under Development" message and wait for a specific key input to break the loop.
    """
    while True:
        kc = keyCode(adcIn)
        bnsd.clear(black)
        bnsd.drawText("Under", light_green, 30, 40)
        bnsd.drawText("Development", light_green, 30, 60)
        bnsd.show()
        if kc == 7:
            break
        time.sleep(0.1)

def us():
    """
    Display "Under Development" message and wait for a specific key input to break the loop.
    """
    while True:
        kc = keyCode(adcIn)
        bnsd.clear(black)
        bnsd.drawText("Under", light_green, 30, 40)
        bnsd.drawText("Development", light_green, 30, 60)
        bnsd.show()
        if kc == 7:
            break
        time.sleep(0.1)

def win():
    """
    Display "You Win!" message and then restart the main menu.
    """
    bnsd.clear(black)
    bnsd.drawText("You Win!", light_green, 50, 50)
    bnsd.show()
    time.sleep(1)
    start()

def lose():
    """
    Display "You Lose!" message and then restart the main menu.
    """
    bnsd.clear(black)
    bnsd.drawText("You Lose!", light_green, 50, 50)
    bnsd.show()
    time.sleep(1)
    start()

def df():
    """
    Display difficulty selection and handle user input to navigate and select a difficulty level.
    """
    time.sleep(0.2)
    difficulty_levels = ["Easy", "Mild", "Hard"]
    current_level = 0

    while True:
        kc = keyCode(adcIn)

        bnsd.clear(black)
        bnsd.drawText("Difficulty", light_green, 40, 20)
        bnsd.drawText("Selection", light_green, 43, 40)
        bnsd.drawUpTriangle(80, 60, 10, dark_green, True)

        current_text = difficulty_levels[current_level]
        bnsd.drawText(current_text, light_green, 65, 80)

        bnsd.drawDownTriangle(80, 110, 10, dark_green, True)
        bnsd.show()

        if kc == 2:
            current_level = (current_level + 1) % len(difficulty_levels)
            bnsd.drawDownTriangle(80, 110, 10, light_green, True)
            bnsd.show()
        elif kc == 0:
            current_level = (current_level - 1) % len(difficulty_levels)
            bnsd.drawUpTriangle(80, 60, 10, light_green, True)
            bnsd.show()
        elif kc == 7:
            break
        elif kc == 6:
            if current_level == 0:
                win()
            else:
                lose()

        time.sleep(0.2)

start()