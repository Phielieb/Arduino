import pyfirmata
import time
from pyfirmata import Arduino

board = Arduino("/dev/ttyACM0")

blink = 13
switch = 10 

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[switch].mode = pyfirmata.INPUT
light = False 

while  True:
    sw = board.digital[switch].read()
    if sw is True and light is False:
        board.digital[blink].write(1)
        light = True 
        time.sleep(0.5)
    sw = board.digital[switch].read()
    if sw and light is True: 
        board.digital[blink].write(0)
        light = False 
        time.sleep(0.5)
    time.sleep(0.1)
    print(sw)

        


