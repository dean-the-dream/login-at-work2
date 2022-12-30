from sys import exit, path
from creds import main_dir
path.append(f"{main_dir}login-at-work2/auto_clicks/")
from gather_images import grab_image
# from navigate_screen import find_and_click

# def catch_error(image):
#     search_again = input(f"""We couldn't find the image found at {image}.
#      Would you like to search for it again?
#     """)
#     if search_again:
#         return search_again
#     exit()

grab_image("already checked in", "already checked in", specificity= "vague")
# find_and_click(click_points["already checked in"])