import serial
import time

def Open():
	ser = serial.Serial('/dev/ttyACM0')
	print ser.name
	ser.write("Open")

def Close():
	ser = serial.Serial('/dev/ttyACM0')
	print ser.name
	ser.write("Close")
