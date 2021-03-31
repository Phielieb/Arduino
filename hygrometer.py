import pyfirmata
import time
import pandas as pd
from pyfirmata import Arduino
from RPLCD.i2c import CharLCD
from datetime import datetime

##Define variables 
lcd_switch = 8
check_switch = 10 
blink = 9

##Load in CSV
try: 
	value_set =pd.read_csv("/home/pi/Arduino/Data/Moist_Val.csv")
	print("CSV file loaded")
except: 
	value_set = pd.DataFrame(columns=["Timestamp","Moist_Val"])
	print("No CSV found, CSV created")

##Define output/input objects
board = Arduino("/dev/ttyACM0")
analog_input = board.get_pin('a:0:i')
board.digital[check_switch].mode = pyfirmata.INPUT

##Launch Info
board.digital[lcd_switch].write(1)
lcd = CharLCD('PCF8574', 0x27)
animations = ["( -_-)","( o_o)","( 0_0)","( ^_^)/","( ^_^)|","( ^_^)/"]
for _ in range(3):
	for animation in animations:
		lcd.write_string("PflanzBot: Rdy \r\n" + animation)
		time.sleep(0.4)
		lcd.clear()
board.digital[lcd_switch].write(0)

def lcd_print(value,show=5):
	board.digital[lcd_switch].write(1)
	lcd = CharLCD('PCF8574', 0x27)  
	lcd.write_string("Moist:"+ str(value)+ "\r\n" +"Len DF: " + str(len(value_set)))	
	time.sleep(show)
	lcd.clear()
	board.digital[lcd_switch].write(0)
	
def check_value():
	switch = board.digital[check_switch].read()
	if switch == True: 
		value = analog_input.read()
		lcd_print(value)
		time.sleep(1)
	time.sleep(0.1)
	
def add_value_to_set():
	board.digital[blink].write(1)
	value = analog_input.read()
	value_set.loc[len(value_set)]=[datetime.now(),value]
	board.digital[blink].write(0)
	value_set.to_csv("./Data/Moist_Val.csv")  

##start Iterator to read analog in 
it = pyfirmata.util.Iterator(board)
it.start()

while True:
	for _ in range(10*3): check_value()
	add_value_to_set()
	

	
