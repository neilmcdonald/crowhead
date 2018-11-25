from microbit import *
import random

# create an empty image
i = Image("00000:"*5)

# loop Indefinitely
while True:
    
    # show the image and wait for 1/10 second
    display.show(i)
    sleep(100)
    
    # move the image up one row
    i = i.shift_up(1)
    
    # choose a random brightness for the now empty bottom row of the display
    for x in range(5):
        i.set_pixel(x, 4, random.randint(3,9))