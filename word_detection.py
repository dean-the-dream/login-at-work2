import easyocr
import pyautogui as pg
import cv2
import screeninfo as si
from navigate_screen import click_and_paste as cnp
from creds import un, password
from time import sleep
from email_integration import get_message as verify


# pass lanuguage arguments to the reader object
reader = easyocr.Reader(['en'], gpu=False)

def img_center(tl,tr,br):
    x_center = ((int(tr[0]) - int(tl[0])) // 2) + int(tl[0])
    y_center = ((int(br[1])- int(tr[1])) // 2) + int(tr[1])
    return (x_center, y_center)

def find_and_click(image_name):
    # capture the entire screen
    sleep(2)
    screenshot = pg.screenshot()

    # save the screenshot picture
    screenshot.save(f"./img/full-screen-shots/{image_name}.png")

    # get a list of coordinate for each word detected
    list_of_words =  reader.readtext(f"./img/full-screen-shots/{image_name}.png")
    print(list_of_words, "<<<<list of words")

    # find the specific word you are looking for 
    current_word = list(filter(lambda x: image_name in x[1], list_of_words))[0]
    print(current_word[0], "<<< current_word")
    

    pg.moveTo(img_center(current_word[0][0], current_word[0][1],current_word[0][2]))
    pg.click()



find_and_click("Heartland")
find_and_click("Username")
cnp(un)
find_and_click("Password")
cnp(password)
find_and_click("Login")
find_and_click("Email")
find_and_click("Send to Email")
pg.press("tab")
cnp(verify())
find_and_click("Continue")


# capture the entire screen
# screenshot = pg.screenshot()

# # save the screenshot picture
# screenshot.save("./img/screenshot.png")

# # get a list of coordinate for each word detected
# list_of_words =  reader.readtext("./img/screenshot.png")
# # print(list_of_words, "<<<<list of words")

# # find the specific word you are looking for
# word_to_detect = "Heartland" 
# current_word = list(filter(lambda x: x[1] == word_to_detect, list_of_words))[0]
# print(current_word[0], "<<< current_word")



# create an immage object
# screenshot_obj = cv2.imread("./img/screenshot.png")
# img = cv2.line(screenshot_obj, (233, 549), (307, 549 ),(255,0,0),2)




# cv2.imshow("window", screenshot_obj)
# cv2.waitKey(0)


