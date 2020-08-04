import pyfirmata
import time
from pyfirmata import Arduino

board = Arduino("COM3")
counter = 0



while counter < 50:
    board.digital[7].write(1)
    time.sleep(0.5)
    board.digital[7].write(0)
    time.sleep(1)

    board.digital[8].write(1)
    time.sleep(1)
    board.digital[8].write(0)
    time.sleep(1)
    counter += 1
    print(counter)
else:
    board.digital[7].write(1)