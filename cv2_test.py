from screeninfo import get_monitors
from word_detection import grab_images, click_points, fill_dict
from pyautogui import press, keyDown, keyUp, scroll, click
from time import sleep
from navigate_screen import find_and_click
from login_logout import get_to_landing_page as navigate
import keyboard
import os

# monitor = 0
# for m in get_monitors():
#     if m.is_primary == True:
#         monitor = m


# win_y = 980
# win_x = 700
# screen_y = int(monitor.height)
# screen_x = int(monitor.width)


# x_start = (screen_x / 2) - (win_x / 2)
# y_start = (screen_y / 2) - (win_y / 2)

# print(f"({x_start},{y_start})")
# print(screen_y)

# screens = wd.screens
# fill_dict(click_points, "./img/")
# from login_logout import get_to_landing_page as navigate

# grab_images("Done","Done")
# find_and_click(click_points["Check Out"])
# sleep(3)
# click()
# print("The mouse has clicked")
# scroll(-500)
# kill_thread = False
# while True:
#     if keyboard.is_pressed("q"):
#         print("You pressed a button")
#         kill_thread = True
#         print(kill_thread)
#         break
# os.makedirs("C:/Program Files/Logio")   
os.makedirs("C:/Coding/Logio/")
        