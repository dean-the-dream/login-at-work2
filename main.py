from os import listdir
import email_integration as el
import login_logout as logio
from login_logout import windows
from login_setup import get_clicks, make_dir
from word_detection import fill_dict, click_points
from creds import main_dir
import sys
import threading



fill_dict(click_points, f"{main_dir}img/")

def thread2(mode, kill_window):
    run_test = True
    match mode:
        case 1:
            logio.sign_in(click_points, test = run_test)
        case 2:
            logio.lunch_sign_out(click_points, test = run_test)
        case 3:
            logio.sign_out(click_points, test = run_test)
        case 4: 
            get_clicks(mode, kill_window, test = run_test)
        case 5: 
            logio.sign_out(click_points, test = run_test)
        case 6:
            get_clicks(mode, kill_window, test = run_test)
        case 7:
            get_clicks(mode, test = run_test)
        case 8:
            get_clicks(mode, test = run_test)
        case _:
            print("Invalid input, try again")
 
    



    # logio.get_to_landing_page(images)

def main():
    mode = logio.choose_mode()
    try:
        fill_dict(click_points, f"{main_dir}img/")
        img_list =  listdir(f"{main_dir}img/full-screen-shots")
    except FileNotFoundError:
        print("""Since this is your first time, we have to map your screen to get a snapshot of the buttons.""")
        logio.open_browser(mode)
        make_dir()
        get_clicks(mode)
   

    start_login = threading.Thread(target=thread2, args = [mode, windows.destroy])
    start_login.daemon = True
    start_login.start()

    # logio.open_browser(mode)
    # sys.exit()
    windows.start()
   
    
if __name__ == "__name__":
    main()

main()