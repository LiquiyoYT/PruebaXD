import os
import cv2
images=[]
path="Images"

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in [".png",".jpg","jpeg"]:
        file_name=path+"/"+file
        images.append(file_name)


frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)

out = cv2.VideoWriter('Proyecto1.mp4',cv2.VideoWriter_fourcc(*'DIVX'),  5, size)

count=len(images)
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Video terminado")
