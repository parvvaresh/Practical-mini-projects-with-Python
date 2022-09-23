import cv2
path = "/content/for_mahsa.mp4"

vidcap = cv2.VideoCapture(path)
success,image = vidcap.read()
count = 0

while success:
  cv2.imwrite("videoframe%d.jpg" % count, image)      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

print("finished")