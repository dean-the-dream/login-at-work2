import easyocr
import pyautogui as pg

# capture the entire screen
screenshot = pg.screenshot()

# save the screenshot picture
screenshot.save("./img/screenshot.png")


# pass lanuguage arguments to the reader object
reader = easyocr.Reader(['en'])
results =  reader.readtext("./img/screenshot.png")
print(results)

# # create an immage object
# screenshot_obj = pg.Image("/img/screenshot.png")

reader = easyocr.Reader(['en'])

