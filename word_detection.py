import easyocr
import pyautogui as pg
import cv2
import screeninfo as si



# capture the entire screen
screenshot = pg.screenshot()

# save the screenshot picture
screenshot.save("./img/screenshot.png")





# pass lanuguage arguments to the reader object
reader = easyocr.Reader(['en'], gpu=False)

# get a list of coordinate for each word detected
list_of_words =  reader.readtext("./img/screenshot.png")
# print(list_of_words, "<<<<list of words")

# find the specific word you are looking for
word_to_detect = "Heartland" 
current_word = list(filter(lambda x: x[1] == word_to_detect, list_of_words))
print(current_word, "<<< current_word")



# create an immage object
screenshot_obj = cv2.imread("./img/screenshot.png")
img = cv2.line(screenshot_obj, (233, 549), (307, 549 ),(255,0,0),2)

def img_center(tl,tr,br):
    x_center = (tr[0] - tl[0]) + tl[0]
    y_center = (br[1]- tr[1]) + tr[1]
    return (x_center, y_center)

pg.moveTo(img_center())
cv2.imshow("window", screenshot_obj)
cv2.waitKey(0)


