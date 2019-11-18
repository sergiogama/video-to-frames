import cv2
vidcap = cv2.VideoCapture('video.mp4')
success, image = vidcap.read()
count = 0
success = True
while success:
    success, image = vidcap.read()
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*10000)) # Um frame a cada 1000 ms (1f/segundo)
    cv2.imwrite("frames/frame%d.jpg" % count, image) # save frame as JPEG file
    count += 1
