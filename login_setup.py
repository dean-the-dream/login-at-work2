from word_detection import grab_images, fill_dict, screens, click_points as cp
import navigate_screen as ns
from time import sleep
from os import path, makedirs
from creds import main_dir, password, un
import sys
from email_integration import get_time
from cv2_test import terminate









def get_clicks(mode, kill_window, test = False, ):
    fill_dict(screens, f"{main_dir}img/full-screen-shots/")

    if not path.exists(cp["Heartland"]):
        grab_images("Heartland","Heartland")
    ns.find_and_click(cp["Heartland"])

    if (not path.exists(cp["Username"])) or (not path.exists(cp["Password"])) or (not path.exists(cp["Login"])):
        grab_images("Login","Username", "Password", "Login")
    ns.find_and_click(cp["Username"])
    ns.click_and_paste(un) 
    

    if not path.exists(cp["recognize the username"]):
        ns.find_and_click(cp["Password"])
        ns.click_and_paste("12345")
        ns.find_and_click(cp["Login"])
        grab_images("recognize the username","recognize the username", specificity = "vague")
    ns.find_and_click(cp["Password"])
    ns.click_and_paste(password)
    kill_window()

    ns.find_and_click(cp["Login"])

    if not path.exists(cp["Email"]):
        grab_images("Email","Email") 
    ns.find_and_click(cp["Email"])

    if not path.exists(cp["Send"]):
        grab_images("Send","Send", instance = 2, specificity="vague")
    ns.find_and_click(cp["Send"])
    time = get_time()

    if not path.exists(cp["Verification Code"]):
        grab_images("Verification Code", "Verification Code")
    ns.enter_verify(cp["Verification Code"], time)

    if not path.exists(cp["Continue"]):
        grab_images("Continue","Continue")
    ns.find_and_click(cp["Continue"])

    if not path.exists(cp["Skip"]):
        grab_images("Skip","Skip")
    ns.find_and_click(cp["Skip"])
    sleep(2)

    
    if (not path.exists(cp["Check In"])) or (not path.exists(cp["Check Out"])):
        grab_images("Welcome","Check In", "Check Out")
    
    

    if (not path.exists(cp["Out"])) or (not path.exists(cp["Meal"])) or (not path.exists(cp["OK"])) or (not path.exists(cp["Cancel"])):
        ns.find_and_click(cp["Check Out"])
        grab_images("Punch","Out","Meal", "OK", "Cancel")
        ns.find_and_click(cp["Cancel"])

    if not path.exists(cp["Check In OK"]):
        ns.find_and_click(cp["Check In"])
        grab_images("Check In OK", "Check In OK", search = "OK")
        ns.find_and_click(cp["Cancel"])


    if mode == 6:
        ns.find_and_click(cp["Check In"])
        
        if not test:
            if  grab_images("already checked in", "already checked in", specificity= "vague") == False:
                ns.find_and_click(cp["Check In OK"])
                grab_images("Done", "Done")
                ns.find_and_click(cp["Done"])
                ns.find_and_click(cp["Check In"])
                grab_images("already checked in", "already checked in")
                ns.find_and_click(cp["Cancel"])
            else:
                grab_images("already checked in", "already checked in", specificity= "vague")
                return "checkedin"
        

    elif mode == 7:
        ns.find_and_click(cp["Check Out"])
        ns.find_and_click(cp["Meal"])
        None if test else ns.find_and_click(cp["OK"])
    elif mode == 8:
        ns.find_and_click(cp["Check Out"])
        ns.find_and_click(cp["Out"])
        None if test else ns.find_and_click(cp["OK"])




def make_dir():
    makedirs(f"{main_dir}img/")
    makedirs(f"{main_dir}img/full-screen-shots")

