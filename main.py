import cv2
import os

path = 'video'
videolist = os.listdir(path)
print(videolist)

i = 1000000000
for j in videolist:
    print(j)
    cap = cv2.VideoCapture(f'{path}/{j}')

    k = 1
    while True:
        k += 1
        ret, frame = cap.read()
        if not ret:
            break
        if k <= 200:
            continue
        k = 0
        cv2.imwrite(f'images/image___{str(i)}.jpg', frame)
        i += 1

