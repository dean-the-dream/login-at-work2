import easyocr
import pyautogui as pg
import cv2
import screeninfo as si
from navigate_screen import find_and_click
from creds import un, password
from time import sleep
from email_integration import get_message as verify
import pyscreenshot as ImageGrab



def main():
    pass

if __name__ == "__name__":
    main()


def fill_dict(dict, img_path):
    for key, value in dict.items():
        name = key.replace(" ", "_")
        dict[key] = f"{img_path}{name}.png"


click_points = {"Heartland":None,
    "Check In": None,
    "Check Out": None,
    "Email": None,
    "Continue": None,
    "Login": None,
    "Username": None,
    "Password": None,
    "Meal": None,
    "OK": None,
    "Out": None,
    "Skip": None,
    "Send to Email": None,
    "Submit": None,
    "Verification Code": None
    }

screens = {
    "Heartland": None,
    "Login": None,
    "Email": None,
    "Send to Email": None,
    "Verification Code": None,
    "Continue": None,
    "Skip": None,


}


def img_center(tl,tr,br):
    x_center = ((int(tr[0]) - int(tl[0])) // 2) + int(tl[0])
    y_center = ((int(br[1])- int(tr[1])) // 2) + int(tr[1])
    return (x_center, y_center)

def img_coordinates(tl,tr,br):
    top = tl[1]
    print(top, "top")
    left = tl[0]
    print(left, "left")
    width = (int(tr[0]) - int(tl[0]))
    print(width, "width")
    height = (int(br[1])- int(tr[1]))
    print(height, "height")
    return (top, left, width, height)


def grab_images(screen_name, *image_list):
    # pass lanuguage arguments to the reader object
    
    reader = easyocr.Reader(['en'], gpu=False)
    # fill_dict(screens, "./img/full-screen-shots/")

    # capture the entire screen
    sleep(2)
    screenshot = pg.screenshot()

    # save the screenshot picture
    screenshot.save(screens[screen_name])

    # get a list of coordinates for each word detected
    list_of_words =  reader.readtext(screens[screen_name])
    print(list_of_words, "<<<<list of words")

    for i, image in enumerate(image_list):
        # find the specific word you are looking for
        word_to_detect = image_list[i]

        # produces a list of the coordinates, surrounding the current word
        current_word = list(filter(lambda x: x[1] == word_to_detect, list_of_words))[0][0]
        print(current_word[0], "<<< current_word")
        image = ImageGrab.grab(bbox = (current_word[0][0], current_word[0][1], current_word[2][0], current_word[2][1]))
        image.save(click_points[image_list[i]])

        print(click_points)