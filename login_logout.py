#############################################################################################
# This module contains the procedurse to sign in or out
###############################################################################################
import navigate_screen as ns
import webview
from gather_images import click_points as cp, fill_dict
from time import sleep
# from creds import un, password, main_dir
# from email_integration import get_time
from screeninfo import get_monitors
# from creds import main_dir
import sys
sys.path
from os import path
def main():
    pass

if __name__ == "__name__":
    main()





class Windows(object):
    def __init__(self) -> None:
        self.background = webview.create_window('BackGround', "https://blankwhitescreen.com/", resizable=False, on_top=False, frameless=True)
        self.main = webview.create_window('Get To Work', "https://www.myworkday.com/wday/authgwy/tsys/login.htmld", resizable=False, width=500, height=700, on_top=True)

    def move(self, window1, window2):
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


def get_to_landing_page(cp):
    ns.find_and_click(cp["Heartland"]) 
    ns.workday_login(cp["Username"],cp["Password"],cp["Login"])
    ns.find_and_click(cp["Email"])
    ns.find_and_click(cp["Send"])
    ns.enter_verify(cp["Verification Code"])
    ns.find_and_click(cp["Continue"])
    ns.find_and_click(cp["Skip"])
    sleep(2)    

def sign_in(images, test = False):
    get_to_landing_page(images)
    ns.find_and_click(images["Check In"])
    None if test else ns.find_and_click(images["OK"])

def lunch_sign_out(images, test = False):
    get_to_landing_page(images)
    ns.find_and_click(images["Check Out"])
    ns.find_and_click(images["Meal"])
    None if test else ns.find_and_click(images["OK"])
    

def sign_out(images, test = False):
    get_to_landing_page(images)
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
    
    match log_mode:
        case 1:
            if (not path.exists(cp["Done"])) or (not path.exists(cp["already checked in"])):
                log_mode = 6
        case 2:
            if not path.exists(cp["Done"]):
                log_mode = 7
        case 3:
            if not path.exists(cp["Done"]):
                log_mode = 8
    return log_mode