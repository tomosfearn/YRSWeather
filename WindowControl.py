import os

def Open():
	os.chdir("/home/marley/YRSWeather/ArduinoCode/Open")
	os.system("sudo ino upload")
def Close():
	os.chdir('/home/marley/YRSWeather/ArduinoCode')
	os.system('sudo ino upload')
