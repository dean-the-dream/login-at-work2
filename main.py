from os import path, mkdir
import login_logout as logio
from navigate_screen import windows
from gather_images import click_points, get_clicks, create_paths
import threading
from sys import exit

run_test = True
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
    windows.destroy()

def main():
    create_paths()
    mode = logio.choose_mode(run_test)
    print(mode)

    start_login = threading.Thread(target=thread2, args = [mode])
    start_login.daemon = True
    start_login.start()
    windows.start()
    
    exit()
    
   
    
if __name__ == "__name__":
    main()

main()