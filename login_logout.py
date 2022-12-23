#############################################################################################
# This module contains the procedurse to sign in or out
###############################################################################################
import navigate_screen as ns
from pyautogui import press
from tkinter import *
import webview
from word_detection import grab_images, fill_dict, screens, click_points as cp
import threading
from time import sleep
from creds import un, password
from email_integration import get_verify_code

def main():
    print()

if __name__ == "__name__":
    main()

def open_browser():
    def move(window):
        # sleep(2)
        window.move(200, 200)
    window = webview.create_window('Get To Work', "https://www.myworkday.com/wday/authgwy/tsys/login.htmld", on_top=True, resizable=False)

    webview.start(move, window)
    
def move_window():
    # print("buttons are pressing")
    # keyDown("winleft")
    # press("d")
    # keyUp("winleft")
    # print("buttons stopped pressing")
    # print("buttons are pressing")
    # keyDown("winleft")
    # keyDown("shift")
    # press("left")
    # press("left")
    # keyUp("winleft")
    # keyUp("shift")
    # print("buttons stopped pressing")
    
    # keyDown("winleft")
    # press("left")
    # keyUp("winleft")
    webview.window
    

def sign_in(images, test = False):
    ns.find_and_click(images[10])
    ns.find_and_click(images[12])
    scroll(-20)
    None if test else ns.find_and_click(images[13])

def lunch_sign_out(images, test = False):
    ns.find_and_click(images[11])
    ns.find_and_click(images[14])
    scroll(-20)
    None if test else ns.find_and_click(images[13])
    

def sign_out(images, test = False):
    ns.find_and_click(images[11])
    ns.find_and_click(images[15])
    scroll(-20)
    None if test else ns.find_and_click(images[13])

def get_to_landing_page(images):
    ns.find_and_click(images[0]) 
    print(images[0])
    ns.workday_login(images[1])
    ns.find_and_click(images[2])
    ns.find_and_click(images[3])
    ns.find_and_click(images[4])
    ns.enter_verify(images[5])
    ns.find_and_click(images[6])
    ns.find_and_click(images[7])
    print("Completed step 7")
    ns.find_and_click(images[9])
    print("completed step 9")


def choose_mode():
    log_mode = int(input("""What Would You like to do?
    1) Login
    2) Logout for Lunch
    3) Logout
    4) Read Screen
    5) Test
    
    Enter Selection: """))
    return log_mode

def get_clicks():
    fill_dict(screens, "./img/full-screen-shots/")
    grab_images("Heartland","Heartland")
    ns.find_and_click(cp["Heartland"])
    grab_images("Login","Username", "Password", "Login")
    ns.find_and_click(cp["Username"])
    ns.click_and_paste(un)
    ns.find_and_click(cp["Password"])
    ns.click_and_paste(password)
    ns.find_and_click(cp["Login"])
    grab_images("Email","Email")
    ns.find_and_click(cp["Email"])
    grab_images("Send to Email","Send to Email")
    ns.find_and_click(cp["Send to Email"])
    grab_images("Verification Code","Verification Code")
    # ns.find_and_click(cp["Verification Code"])
    press("tab")
    ns.click_and_paste(get_verify_code())
    grab_images("Continue","Continue")
    ns.find_and_click(cp["Continue"])



# def get_to_landing_page(images):
#     open_browser()
#     ns.find_and_click(images[0]) 
#     print(images[0])
#     ns.workday_login(images[1])
#     ns.find_and_click(images[2])
#     ns.find_and_click(images[3])
#     ns.find_and_click(images[4])
#     ns.enter_verify(images[5])
#     ns.find_and_click(images[6])
#     ns.find_and_click(images[7])
#     print("Completed step 7")
#     ns.find_and_click(images[9])
#     print("completed step 9")