from RPLCD.i2c import CharLCD
import pyfirmata
from pyfirmata import Arduino
import time

board = Arduino("/dev/ttyACM0")
board.digital[8].write(1)

lcd = CharLCD('PCF8574', 0x27)   	

#lcd.write_string('Ich spiele\r\ncyberpunk!')		

while True: 
	board.digital[8].write(1)
	lcd = CharLCD('PCF8574', 0x27)   
	print("open")
	lcd.write_string('Ich liebe sonja!')		
	time.sleep(3)
	board.digital[8].write(0)
	print("closed")

	time.sleep(2)
	

