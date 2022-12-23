import os
from navigate_screen import arrange_photos as sort_pics
import email_integration as el
import login_logout as logio
from time import sleep
from word_detection import fill_dict, click_points
import threading

fill_dict(click_points, "./img/")
img_list =  os.listdir("./img")
images = sort_pics(img_list, 'heartland_button.png', 'login_welcome.png', 'login_button.png', 'choose_email_auth.png', 'send_to_email.png', 'verify_code.png','continue_button.png', "remember_check_box.png", "global_pay_logo.png", "submit.png", "check_in.png", "check_out.png", "details.png", "ok.png", "meal.png", "out.png")

def thread2():
    # mode = logio.choose_mode()
    mode = 4

    match mode:
        case 1:
            logio.sign_in(images)
        case 2:
            logio.lunch_sign_out(images)
        case 3:
            logio.sign_out(images)
        case 4: 
            logio.get_clicks()
        case 5: 
            logio.sign_out(images, True)
    


    # logio.get_to_landing_page(images)

def main():
    start_login = threading.Thread(target=thread2)
    start_login.start()
    logio.open_browser()
    

    
    

    



   
    
if __name__ == "__name__":
    main()

main()