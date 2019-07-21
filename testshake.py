# 在这里写上你的代码 :-)
from microbit import *

while True :
    display.show(Image.DIAMOND)
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.show(Image.YES)
        sleep(1000)
