import pyfirmata
import time
from pyfirmata import Arduino

board = Arduino("COM3")

blink = 10


it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:4:i')
value = 0.3

while  True:
    value = 0.3 if analog_input.read() == None else analog_input.read()
    time.sleep(0.01)
    print(value)
    if value < 0.2:
        board.digital[blink].write(1)
    else:
        board.digital[blink].write(0)
        


