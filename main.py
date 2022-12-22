import os
from navigate_screen import arrange_photos as sort_pics
import email_integration as el
import login_logout as logio
import threading





def main():
    img_list =  os.listdir("./img")
    images = sort_pics(img_list, 'heartland_button.png', 'login_welcome.png', 'login_button.png', 'choose_email_auth.png', 'send_to_email.png', 'verify_code.png','continue_button.png', "remember_check_box.png", "global_pay_logo.png", "submit.png", "check_in.png", "check_out.png", "details.png", "ok.png", "meal.png", "out.png")
    def runner():
        return logio.get_to_landing_page(images)
        
    logio.open_browser()

    t1 = threading.Thread(target=runner)
    t1.start()
    
    log_mode = int(input("""What Would You like to do?
    1) Login
    2) Logout for Lunch
    3) Logout
    4) Test
    
    Enter Selection: """))

    logio.get_to_landing_page(images)
    

    match log_mode:
        case 1:
            logio.sign_in(images)
        case 2:
            logio.lunch_sign_out(images)
        case 3:
            logio.sign_out(images)
        case 4: 
            logio.sign_out(images, True)



   
    
if __name__ == "__name__":
    main()

main()