import serial
def Open():
	ser = serial.Serial(0)
	print ser.name
	ser.write("Open")

def Close():
	ser = serial.Serial(0)
	print ser.name
	ser.write("Close")
