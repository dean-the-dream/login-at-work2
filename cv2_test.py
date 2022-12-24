from screeninfo import get_monitors
from word_detection import grab_images, click_points, fill_dict
from pyautogui import press, keyDown, keyUp, scroll, click
from time import sleep

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
# grab_images("Send","Send", instance = 2, search="vague")
sleep(3)
click()
print("The mouse has clicked")
scroll(-500)
