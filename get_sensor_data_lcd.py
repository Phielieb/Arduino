from RPLCD.i2c import CharLCD
import random

lcd = CharLCD('PCF8574', 0x27)   	

lcd.write_string("jonas ist doof")		

