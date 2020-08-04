import pyfirmata
import time
from pyfirmata import Arduino

piep = 8
blink = 7

board = Arduino("COM3")
counter = 0

while counter < 2:
    board.digital[blink].write(1)
    time.sleep(1)
    board.digital[blink].write(0)
    time.sleep(1)

    board.digital[piep].write(1)
    time.sleep(1)
    board.digital[piep].write(0)
    time.sleep(1)
    counter += 1
    print(counter)
else:
    board.digital[blink].write(1)