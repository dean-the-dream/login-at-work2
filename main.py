import os
from navigate_screen import arrange_photos as sort_pics
import email_integration as el
import login_logout as logio
from time import sleep
from word_detection import fill_dict, click_points
import threading
import keyboard
from login_setup import make_dir
from creds import main_dir



# images = sort_pics(img_list, 'heartland_button.png', 'login_welcome.png', 'login_button.png', 'choose_email_auth.png', 'send_to_email.png', 'verify_code.png','continue_button.png', "remember_check_box.png", "global_pay_logo.png", "submit.png", "check_in.png", "check_out.png", "details.png", "ok.png", "meal.png", "out.png")


def thread2(mode):

    
    if not mode == 4:
        logio.get_to_landing_page(click_points)
        match mode:
            case 1:
                logio.sign_in(click_points)
            case 2:
                logio.lunch_sign_out(click_points)
            case 3:
                logio.sign_out(click_points)
            case 4: 
                logio.get_clicks()
            case 5: 
                logio.lunch_sign_out(click_points, test=True)
    elif mode == 4:
        logio.get_clicks()
    else:
        print("Invalid input, try again")
 
    



    # logio.get_to_landing_page(images)

def main():
    mode = logio.choose_mode()
    try:
        fill_dict(click_points, f"{main_dir}img/")
        img_list =  os.listdir(f"{main_dir}img/")
    except FileNotFoundError:
        print("""Since this is your first time, we have to map your screen to get a snapshot of the buttons.""")
        logio.open_browser(mode)
        make_dir()
        logio.get_clicks()
   

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