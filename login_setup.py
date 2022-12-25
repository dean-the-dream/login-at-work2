from word_detection import grab_images, fill_dict, screens, click_points as cp
import navigate_screen as ns
from time import sleep
import os
from creds import main_dir



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

def make_dir():
    os.makedirs(f"{main_dir}img2/")
    os.makedirs(f"{main_dir}img2/full-screen-shots")
# if not complete_capture:

    