#############################################################################################
# This module contains the procedurse to sign in or out
###############################################################################################
import navigate_screen as ns
from pyautogui import scroll
from tkinter import *
import webview
from word_detection import grab_images as gb
import threading

def main():
    print()

if __name__ == "__name__":
    main()

def open_browser():
    webview.create_window('Get To Work', "https://www.myworkday.com/wday/authgwy/tsys/login.htmld", on_top=True, resizable=False)
    
    webview.start()
    webview.window.moveTo(640, 360)

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