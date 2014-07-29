from serial import Serial

ser = Serial('/dev/ttyUSB0', 9600)

x=ser.readline()
ser.write('1')
