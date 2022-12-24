#############################################################################################
# This module contains the procedurse to sign in or out
###############################################################################################
import navigate_screen as ns
from pyautogui import press, keyDown, keyUp, scroll, click
from tkinter import *
import webview
from word_detection import grab_images, fill_dict, screens, click_points as cp
from time import sleep
from creds import un, password
from email_integration import get_verify_code as get_code
from screeninfo import get_monitors


def main():
    print()

if __name__ == "__name__":
    main()

def open_browser():
    monitors = get_monitors

    def move(window, background):
        background.move(0,0)
        background.resize(1920, 1080)
        # sleep(1)
        window.move(610, 50)
        window.resize(800, 1000)
        # window.show()

    background = webview.create_window('BackGround', "https://blankwhitescreen.com/", resizable=False, on_top=False, frameless=True)
    window = webview.create_window('Get To Work', "https://www.myworkday.com/wday/authgwy/tsys/login.htmld", resizable=False, width=500, height=700, on_top=True)

    # webview.start()
    webview.start(move,(window,background))

    

def sign_in(images, test = False):
    ns.find_and_click(images["Check In"])
    None if test else ns.find_and_click(images["OK"])

def lunch_sign_out(images, test = False):
    ns.find_and_click(images["Check Out"])
    ns.find_and_click(images["Meal"])
    None if test else ns.find_and_click(images["OK"])
    

def sign_out(images, test = False):
    ns.find_and_click(images["Check Out"])
    ns.find_and_click(images["Out"])
    None if test else ns.find_and_click(images["OK"])


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
    grab_images("Send","Send", instance = 2, search="vague")
    ns.find_and_click(cp["Send"])
    grab_images("Verification Code", "Verification Code")
    ns.enter_verify(cp["Verification Code"])
    grab_images("Continue","Continue")
    ns.find_and_click(cp["Continue"])
    grab_images("Skip","Skip")
    ns.find_and_click(cp["Skip"])
    sleep(2)
    grab_images("Welcome","Check In", "Check Out")
    ns.find_and_click(cp["Check Out"])
    grab_images("Punch","Out","Meal", "OK")
    



def get_to_landing_page(cp):
    ns.find_and_click(cp["Heartland"]) 
    ns.workday_login(cp["Username"],cp["Password"],cp["Login"])
    ns.find_and_click(cp["Email"])
    ns.find_and_click(cp["Send"])
    ns.enter_verify(cp["Verification Code"])
    ns.find_and_click(cp["Continue"])
    ns.find_and_click(cp["Skip"])
    sleep(2)
    
