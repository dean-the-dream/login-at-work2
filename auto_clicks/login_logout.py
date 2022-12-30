#############################################################################################
# This module contains the procedurse to sign in or out
###############################################################################################
import auto_clicks.navigate_screen as ns
import gather_images as gi
from time import sleep
from screeninfo import get_monitors
from os.path import exists
def main():
    pass

if __name__ == "__name__":
    main()

cp = gi.click_points

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
    print("Sign In Works")
    if (not exists(cp["Done"])) or (not exists(cp["already checked in"])):
        gi.get_clicks("sign_in", test)
    else:
        get_to_landing_page(images)
        ns.find_and_click(images["Check In"])
        None if test else ns.find_and_click(images["OK"])

def lunch_sign_out(images, test = False):
    if not exists(cp["Done"]):
        gi.get_clicks("lunch", test)
    else:
        get_to_landing_page(images)
        ns.find_and_click(images["Check Out"])
        ns.find_and_click(images["Meal"])
        None if test else ns.find_and_click(images["OK"])
    

def sign_out(images, test = False):
    if not exists(cp["Done"]):
        gi.get_clicks("sign_out", test)
    else:
        get_to_landing_page(images)
        ns.find_and_click(images["Check Out"])
        ns.find_and_click(images["Out"])
        None if test else ns.find_and_click(images["OK"])


def choose_mode(test):
    message = "THIS IS A TEST!" if test else "This is NOT a test!"
    log_mode = int(input(f"""What Would You like to do?
    1) Login
    2) Logout for Lunch
    3) Logout
    4) Read Screen
    
    {message}
    
    Enter Selection: """))
   
    return log_mode