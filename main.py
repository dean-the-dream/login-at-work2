from os import path, listdir
from navigate_screen import arrange_photos as sort_pics
import email_integration as el
import login_logout as logio
from login_setup import get_clicks, make_dir
from word_detection import fill_dict, click_points
import threading
import keyboard
from creds import main_dir



# images = sort_pics(img_list, 'heartland_button.png', 'login_welcome.png', 'login_button.png', 'choose_email_auth.png', 'send_to_email.png', 'verify_code.png','continue_button.png', "remember_check_box.png", "global_pay_logo.png", "submit.png", "check_in.png", "check_out.png", "details.png", "ok.png", "meal.png", "out.png")


def thread2(mode):
    match mode:
        case 1:
            if not path.exists(click_points["already checked in"]):
                get_clicks(mode)
            else:
                logio.sign_in(click_points)
        case 2:
            if not path.exists(click_points["Check In OK"]):
                get_clicks(mode)
            else:
                logio.lunch_sign_out(click_points)
        case 3:
            if not path.exists(click_points["Check In OK"]):
                get_clicks(mode)
            else:
                logio.sign_out(click_points)
        case 4: 
            get_clicks(1)
        case 5: 
            logio.sign_out(click_points, test=True)
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
        get_clicks(1)
   

    start_login = threading.Thread(target=thread2, args = [mode])
    start_login.start()
    logio.open_browser(mode)
    while True:
        if keyboard.is_pressed("q"):
            print("You pressed a button")
            kill_thread = True
            print(kill_thread)
        
   
    
if __name__ == "__name__":
    main()

main()