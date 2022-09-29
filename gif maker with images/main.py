import imageio

import cv2 as cv

path = "C:\\Users\\Administrator\\Desktop\\My code\\PYTHON\simple project\\gif maker with images\\photo\\"


filenames = [path + "1.png", path + "2.png", path + "3.png"]


images = []

for filename in filenames:
    images.append(cv.imread(filename))
    
imageio.mimsave("test.gif", images, 'GIF', duration=1)

print("finished")

