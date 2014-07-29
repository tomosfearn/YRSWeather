from nanpy import (ArduinoApi, SerialManager)

connection = SerialManager()
a = ArduinoApi(connection=connection)
a.pinMode(13, a.OUTPUT)
a.digitalWrite(13, a.HIGH)
