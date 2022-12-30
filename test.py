from sys import exit

def catch_error(image):
    search_again = input(f"""We couldn't find the image found at {image}.
     Would you like to search for it again?
    """)
    if search_again:
        return search_again
    exit()