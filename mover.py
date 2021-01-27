from autopy import mouse
import time

while True:
    x,y = mouse.location()
    mouse.move(x+1,y+1)
    time.sleep(60*10)
