import cv2
import time
from OpencvRingBuffer import OpencvRingBuffer

cap = cv2.VideoCapture(0)

buff=OpencvRingBuffer(cap)#建立OpencvRingBuffer
buff.startcap()#开启线程捕捉

time.sleep(1)#假如你的算法导致1s延迟
ret,frame=buff.getnew()#获得最新帧
print(time.time())
cv2.imwrite("captest1.jpg", frame)

time.sleep(1)#假如你的算法导致1s延迟
ret,frame=buff.getnew()
print(time.time())
cv2.imwrite("captest2.jpg", frame)

time.sleep(1)#假如你的算法导致1s延迟
ret,frame=buff.getnew()
print(time.time())
cv2.imwrite("captest3.jpg", frame)

buff.stopcap()