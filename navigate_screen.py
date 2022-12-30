import webview
import time
import os
import creds
import pyautogui as pg
import time
from email_integration import get_verify_code as get_code
from gather_images import click_points as cp
from os.path import exists


#############################################################################################
#This module contains all the methods to navigate to the main final workday landing page before signing in or out
###############################################################################################

#funtion pastes a text wherever the cursor is currently located
def click_and_paste(text, click = True):

    pg.click() if click else None
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

    pg.keyDown('ctrl')
    pg.press('a')
    pg.keyUp('ctrl')
    pg.press('backspace')
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')

# function to find images on the screen
def locate_image(image_path):
    # create the path to the image in the images folder
    # image_path = f"./img/{image_path}"

    # store the image in a variable
    image_location = pg.locateCenterOnScreen(image_path, confidence=.8) 
    print(image_location, "location")
    # wait for thirty second while python finds the center of the button
    timeout = time.time() + 30
    while image_location is None:
        image_location = pg.locateCenterOnScreen(image_path) 
        if time.time() > timeout:
            print("Something went wrong", "move and click timed out")
            break
    return image_location

# find the heartland button and click it
def find_and_click(image_path, delay=0):
    print(f"Clicking image at path: '{image_path}'...")
    delay if time.sleep(delay) else None
    image_center = locate_image(image_path)
    #move the mouse to the center of the button
    pg.moveTo(image_center)

    #mouseclick
    pg.click()
    
    # print(image_path)
    # print(image_center)
    # ##############################################################################
    # #The purpose of this code is to make sure that the images can be used, no matter what computer, by converting the color space. I have to understand it later, let me get it to work on this computer first.
    # #take a screenschot to locate the image
    # image_location = pg.screenshot()
    # # adjust color space
    # image_location = cv2.cvtColor(np.array(image_location), cv2.COLOR_RGB2BGR)
    # #locate heartlandbutton on the screen
    # ################################################################################

# enter username and password inworkday
def workday_login(username, password, login):
    username = locate_image(username)
    password = locate_image(password)
    login = locate_image(login)

    # move the mouse to the center of username input box
    pg.moveTo(username)
    click_and_paste(creds.un)

    # move the mouse to the center of password input box
    pg.moveTo(password)
    click_and_paste(creds.password)
    
    #click on login button
    pg.moveTo(login)
    pg.click()

# copy and past verify code
def enter_verify(image_path, time = None):
    center_image = locate_image(image_path)

    # move the mouse to the center of username input box
    pg.moveTo(center_image[0], center_image[1] + 40)
    click_and_paste(get_code(time if time else None))

# rearrange a list of pictures to ensure they are always in the intended order    
def arrange_photos(img_list, *img_group):
    
    print(img_list)
    count = 0
    result = img_list
    while count < len(img_group):
        item = result.pop(result.index(img_group[count]))
        result.insert(count, item)
        count += 1
        
    return result  


class Windows(object):
    def __init__(self) -> None:
        self.background = webview.create_window('BackGround', "https://blankwhitescreen.com/", resizable=False, on_top=False, frameless=True)
        self.main = webview.create_window('Get To Work', "https://www.myworkday.com/wday/authgwy/tsys/login.htmld", resizable=False, width=500, height=700, on_top=True)


    def move(self, window1, window2):
        if (not exists(cp["Done"])) or (not exists(cp["already checked in"])):
            window1.move(0,0)
            window1.resize(1920, 1080)
        window2.move(610, 10)
        window2.resize(800, 1000)

    def destroy(self):
        self.background.destroy()
        self.main.destroy()

    def start(self):
        webview.start(self.move,(self.background,self.main))

windows = Windows()