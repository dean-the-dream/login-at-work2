from cv2 import imread, imshow, waitKey

screen = "./img/full-screen-shots/Heartland.png"
screenimg = imread(screen)
imshow("screen", screenimg)
