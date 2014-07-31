import os
from optparse import OptionParser
parser = OptionParser()

parser.add_option("-O","--open",help='Open or no')
def Open():
	os.chdir("/home/marley/YRSWeather/ArduinoCode/Open")
	os.system("sudo ino upload")
def Close():
	os.chdir('/home/marley/YRSWeather/ArduinoCode/Close')
	os.system('sudo ino upload')
