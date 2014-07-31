#Used for starting the flask server
from flask import Flask #Import flask mains
from flask import request #Import flask requests
from flask import render_template #Import flask render templates
from flask import url_for
import json, urllib #import api modules
import time #Imporing time in darlek voice
import WindowControl
OldTemp = 'banana'
app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("my-form.html") #Set render template

OldTemp = 'banana'

@app.route('/', methods=['POST']) #Set the route
def my_form_post():
    global OldTemp
    text = request.form['text']
    while True:
    	url = "http://api.openweathermap.org/data/2.5/weather?q=" + text #Download the json
    	response = urllib.urlopen(url) #Download Json
    	data = json.loads(response.read()) #Parse json
	while data['main']['temp'] != OldTemp:
		OldTemp = data['main']['temp']
		if data['weather'][0]['description'].find("rain") > 0:
			WindowControl.Close()
		elif data['main']['temp'] > 298.15:
			WindowControl.Open()   
 		print("Current Weather in " + text + " " + data['weather'][0]['description']) #Debug infomation
    		print("Temp: " + str(data['main']['temp'])) #Print temp 
if __name__ == '__main__':
    app.debug = True #Uncomment to enable debugging
    app.run(host='0.0.0.0') #Run the Server
