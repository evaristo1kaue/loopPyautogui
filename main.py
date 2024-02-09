from pyautogui import alert
from pyautogui import click
from pyautogui import position
from pyperclip import copy
from time import sleep

secs = 0.1
loops = 0

alert('The code will start')

sleep(2)
position = position()
print(position)

while loops < 40:

    sleep(secs)

    # Clicking
    click(insert the position x and y)

    loops += 1

# The final click
click(insert the position x and y)
