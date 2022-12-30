from creds import main_dir
from sys import exit, path
path.append(f"{main_dir}login-at-work2/auto_clicks/")
from os import path, mkdir
import login_logout as logio # type:ignore
from auto_clicks.navigate_screen import windows
from gather_images import click_points, get_clicks, create_paths # type:ignore
import threading
from uix_app import run_uix, option
from waiting import wait
from time import sleep






run_test = False
def thread2(mode):
    match mode:
        case 1:
            logio.sign_in(click_points, test = run_test)
        case 2:
            logio.lunch_sign_out(click_points, test = run_test)
        case 3:
            logio.sign_out(click_points, test = run_test)
        case 4: 
            get_clicks(mode, run_test)
        case _:
            print("Invalid input, try again")
def thread3():
    run_uix()

def main():
    mode = 0
    create_paths()
    
    start_kivy = threading.Thread(target=thread3)
    start_kivy.start()
    
    print("Waiting for mode")
    wait(lambda: not option.mode == 0)
    mode=option.mode
    print("Recieved mode")
    print(mode)

    start_login = threading.Thread(target=thread2, args = [mode])
    start_login.daemon = True
    start_login.start()
    windows.start()
    
    exit()
    
   
    
if __name__ == "__name__":
    main()

main()