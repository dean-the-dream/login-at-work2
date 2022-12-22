import webbrowser
import time
import os
import creds
import pyautogui as pg
import time
from email_integration import get_verify_code as get_code


#############################################################################################
#This module contains all the methods to navigate to the main final workday landing page before signing in or out
###############################################################################################
def open_browser():
    url = "https://www.myworkday.com/wday/authgwy/tsys/login.htmld"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito"
    webbrowser.get(chrome_path).open_new(url)
    # webbrowser.open_new(url)

#funtion pastes a text wherever the cursor is currently located
def click_and_paste(text):

    pg.click()
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
    image_path = f"./img/{image_path}"

    # store the image in a variable
    image_location = pg.locateCenterOnScreen(image_path, confidence=.7) 
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
    print(image_path)
    print(delay, "delay")
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
def workday_login(image_path):
    center_image = locate_image(image_path)

    # move the mouse to the center of username input box
    pg.moveTo(center_image[0], center_image[1] + 96)
    click_and_paste(creds.un)

    # move the mouse to the center of password input box
    pg.moveTo(center_image[0], center_image[1] + 156)
    click_and_paste(creds.password)
    
    #click on login button
    pg.moveTo(center_image[0], center_image[1] + 216)
    pg.click()

# copy and past verify code
def enter_verify(image_path):
    center_image = locate_image(image_path)

    # move the mouse to the center of username input box
    pg.moveTo(center_image[0], center_image[1] + 40)
    click_and_paste(get_code())

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

}

# # check if workdaay remembers this device or not
# def check_for_remember(remeber_device, login_page):
#     remeber_device1 = f"./img/{remeber_device}"
#     login_page1 = f"./img/{login_page}"
#     remember = None
#     login = None

#     timeout = time.time() + 30
#     while (remember is None) and (login is None):
#         remember = pg.locateCenterOnScreen(remeber_device1, confidence=.7)
#         if remember: 
#             return True
#         login = pg.locateCenterOnScreen(login_page1, confidence=.7) 
#         if login:
#             return False
#         if time.time() > timeout:
#             print("Something went wrong", "check for remember timed out")
#             break
