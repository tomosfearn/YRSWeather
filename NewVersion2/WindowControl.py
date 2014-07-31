import os
import serial
ser = serial.Serial(baudrate=9600,port='/dev/ttyACM0')

def Open():
	print ser.name
	ser.write("O")

def Close():
	print ser.name
	ser.write("C")
