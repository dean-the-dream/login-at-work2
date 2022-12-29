import easyocr
from pyautogui import screenshot 
from creds import un, password, main_dir
from time import sleep
import pyscreenshot as ImageGrab
import navigate_screen as ns
from os import path, makedirs
from email_integration import get_time



# def main():
#     pass

# if __name__ == "__name__":
#     main()



# fills a dictionary with paths for images, to be referenced 
def fill_dict(dict, img_path):
    for key, value in dict.items():
        name = key.replace(" ", "_")
        dict[key] = f"{img_path}{name}.png"

# a dictionary for referencing points to click
click_points = {"Heartland":None,
    "Check In": None,
    "Check Out": None,
    "Email": None,
    "Continue": None,
    "Login": None,
    "Username": None,
    "Password": None,
    "Meal": None,
    "OK": None,
    "Out": None,
    "Skip": None,
    "Send": None,
    "Submit": None,
    "Verification Code": None,
    "Check In": None,
    "Check Out": None,
    "Done": None,
    "recognize the username": None,
    "Check In OK": None,
    "already checked in": None,
    "Cancel": None

    }

# a dictionary for referencing screen shots
screens = {
    "Heartland": None,
    "Login": None,
    "Email": None,
    "Verification Code": None,
    "Continue": None,
    "Skip": None,
    "Send": None,
    "Welcome": None,
    "Punch": None,
    "Done": None,
    "recognize the username": None,
    "Check In OK": None,
    "Cancel": None,
    "already checked in": None
}



fill_dict(screens, f"{main_dir}img/full-screen-shots/")
fill_dict(click_points, f"{main_dir}img/")

# a function to get an image of a speficified word
def grab_image(screen_name, *image_list,  specificity = "explicit", instance = 1, search = None):
    instance = instance - 1
    # pass lanuguage arguments to the reader object
    
    reader = easyocr.Reader(['en'], gpu=False)
    fill_dict(screens, f"{main_dir}img/full-screen-shots/")

    # capture the entire screen
    sleep(2)
    screenshot = screenshot()

    # save the screenshot picture
    screenshot.save(screens[screen_name])

    # get a list of coordinates for each word detected
    list_of_words =  reader.readtext(screens[screen_name])
    print(list_of_words, "<<<<list of words")

    for i, image in enumerate(image_list):
        # find the specific word you are looking for
        word_to_detect = search if search else image_list[i]

        # produces a list of the coordinates, surrounding the current word
        try:
            current_word = list(filter(lambda x: 
            (word_to_detect in x[1])
            if specificity == "vague"
            else x[1] == word_to_detect, 
            list_of_words))[instance][0]
        except IndexError:
            print(word_to_detect, "<<< current_word")
            print("word not found")
            return False
        # current_word = list(filter(lambda x: word_to_detect in x[1] , list_of_words))[instance][0]
        
        
        image = ImageGrab.grab(bbox = (current_word[0][0], current_word[0][1], current_word[2][0], current_word[2][1]))
        image.save(click_points[image_list[i]])

        print(click_points, "<<<< click points")



def get_clicks(mode, kill_window, test = False, ):

    if not path.exists(click_points["Heartland"]):
        grab_image("Heartland","Heartland")
    ns.find_and_click(click_points["Heartland"])

    if (not path.exists(click_points["Username"])) or (not path.exists(click_points["Password"])) or (not path.exists(click_points["Login"])):
        grab_image("Login","Username", "Password", "Login")
    ns.find_and_click(click_points["Username"])
    ns.click_and_paste(un) 
    

    if not path.exists(click_points["recognize the username"]):
        ns.find_and_click(click_points["Password"])
        ns.click_and_paste("12345")
        ns.find_and_click(click_points["Login"])
        grab_image("recognize the username","recognize the username", specificity = "vague")
    ns.find_and_click(click_points["Password"])
    ns.click_and_paste(password)
    kill_window()

    ns.find_and_click(click_points["Login"])

    if not path.exists(click_points["Email"]):
        grab_image("Email","Email") 
    ns.find_and_click(click_points["Email"])

    if not path.exists(click_points["Send"]):
        grab_image("Send","Send", instance = 2, specificity="vague")
    ns.find_and_click(click_points["Send"])
    time = get_time()

    if not path.exists(click_points["Verification Code"]):
        grab_image("Verification Code", "Verification Code")
    ns.enter_verify(click_points["Verification Code"], time)

    if not path.exists(click_points["Continue"]):
        grab_image("Continue","Continue")
    ns.find_and_click(click_points["Continue"])

    if not path.exists(click_points["Skip"]):
        grab_image("Skip","Skip")
    ns.find_and_click(click_points["Skip"])
    sleep(2)

    
    if (not path.exists(click_points["Check In"])) or (not path.exists(click_points["Check Out"])):
        grab_image("Welcome","Check In", "Check Out")
    
    

    if (not path.exists(click_points["Out"])) or (not path.exists(click_points["Meal"])) or (not path.exists(click_points["OK"])) or (not path.exists(click_points["Cancel"])):
        ns.find_and_click(click_points["Check Out"])
        grab_image("Punch","Out","Meal", "OK", "Cancel")
        ns.find_and_click(click_points["Cancel"])

    if not path.exists(click_points["Check In OK"]):
        ns.find_and_click(click_points["Check In"])
        grab_image("Check In OK", "Check In OK", search = "OK")
        ns.find_and_click(click_points["Cancel"])


    if mode == 6:
        ns.find_and_click(click_points["Check In"])
        
        if not test:
            if  grab_image("already checked in", "already checked in", specificity= "vague") == False:
                ns.find_and_click(click_points["Check In OK"])
                grab_image("Done", "Done")
                ns.find_and_click(click_points["Done"])
                ns.find_and_click(click_points["Check In"])
                grab_image("already checked in", "already checked in")
                ns.find_and_click(click_points["Cancel"])
            else:
                grab_image("already checked in", "already checked in", specificity= "vague")
                return "checkedin"
        

    elif mode == 7:
        ns.find_and_click(click_points["Check Out"])
        ns.find_and_click(click_points["Meal"])
        None if test else ns.find_and_click(click_points["OK"])
    elif mode == 8:
        ns.find_and_click(click_points["Check Out"])
        ns.find_and_click(click_points["Out"])
        None if test else ns.find_and_click(click_points["OK"])




# def make_dir():
#     makedirs(f"{main_dir}img/")
#     makedirs(f"{main_dir}img/full-screen-shots")
