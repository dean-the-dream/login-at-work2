from os import listdir
from navigate_screen import arrange_photos as sort_pics
import email_integration as el
import login_logout as logio
from login_setup import get_clicks, make_dir
from word_detection import fill_dict, click_points
import threading
import keyboard
from creds import main_dir
import sys



# images = sort_pics(img_list, 'heartland_button.png', 'login_welcome.png', 'login_button.png', 'choose_email_auth.png', 'send_to_email.png', 'verify_code.png','continue_button.png', "remember_check_box.png", "global_pay_logo.png", "submit.png", "check_in.png", "check_out.png", "details.png", "ok.png", "meal.png", "out.png")


def thread2(mode):
    match mode:
        case 1:
            logio.sign_in(click_points, test=True)
        case 2:
            logio.lunch_sign_out(click_points, test=True)
        case 3:
            logio.sign_out(click_points, test=True)
        case 4: 
            get_clicks(mode)
        case 5: 
            logio.sign_out(click_points, test=True)
        case 6:
            get_clicks(mode, test=True)
        case 7:
            get_clicks(mode, test=True)
        case 8:
            get_clicks(mode, test=True)
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
   

    start_login = threading.Thread(target=thread2, args = [mode])
    start_login.daemon = True
    start_login.start()
    logio.open_browser(mode)
    sys.exit()
        
   
    
if __name__ == "__name__":
    main()

main()