from word_detection import grab_images, fill_dict, screens, click_points as cp
import navigate_screen as ns
from time import sleep
import os
from creds import main_dir, password, un
import sys
from email_integration import get_time






def get_clicks( test = False):
    completed = 0
    step = 0
    fill_dict(screens, f"{main_dir}img/full-screen-shots/")

    if completed < [1]:
        grab_images("Heartland","Heartland")
        steps += 1
    ns.find_and_click(cp["Heartland"])

    if completed < [2]:
        grab_images("Login","Username", "Password", "Login")
        steps += 1
    ns.find_and_click(cp["Username"])
    ns.click_and_paste(un) 

    if completed < [3]:
        ns.find_and_click(cp["Password"])
        ns.click_and_paste(12345)
        ns.find_and_click(cp["Login"])
        grab_images("recognize","recognize the username", search = "vague")
    ns.click_and_paste(password)
    ns.find_and_click(cp["Login"])

    if completed < [4]:
        grab_images("Email","Email")
        steps += 1
    ns.find_and_click(cp["Email"])

    if completed < [5]:
        grab_images("Send","Send", instance = 2, search="vague")
        steps += 1
    ns.find_and_click(cp["Send"])
    time = get_time()

    if completed < [6]:
        grab_images("Verification Code", "Verification Code")
        steps += 1
    ns.enter_verify(cp["Verification Code"], time)

    if completed < [7]:
        grab_images("Continue","Continue")
        steps += 1
    ns.find_and_click(cp["Continue"])

    if completed < [8]:
        grab_images("Skip","Skip")
        steps += 1
    ns.find_and_click(cp["Skip"])
    sleep(2)

    if completed < [9]:
        grab_images("Welcome","Check In", "Check Out")
        steps += 1
    ns.find_and_click(cp["Check Out"])

    if completed < [10]:
        grab_images("Punch","Out","Meal", "OK", "Cancel")
        steps += 1 
    ns.find_and_click(cp["Cancel"])
    ns.find_and_click(cp["Check In"])


    if (completed < [11]) and not test:
        ns.find_and_click(cp["OK"])
        grab_images("Done","Done")
        ns.find_and_click(cp["Check In"])
        # grab_images("Punch","Out","Meal", "OK", "Cancel")
    if not test:
        file = open("progress.py")
        for line in file:
            if steps in line:
                steps



def make_dir():
    os.makedirs(f"{main_dir}img2/")
    os.makedirs(f"{main_dir}img2/full-screen-shots")

print(data)