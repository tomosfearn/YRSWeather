from serial import Serial

ser = Serial('/dev/ttyAMA0', 9600)

x=ser.readline()
ser.write('1')
