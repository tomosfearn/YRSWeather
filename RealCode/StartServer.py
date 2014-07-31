#Used for starting the flask server
from flask import Flask #Import flask mains
from flask import request #Import flask requests
from flask import render_template #Import flask render templates
from flask import url_for
import json, urllib #import api modules
import time #Imporing time in darlek voice
import WindowControl

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("my-form.html") #Set render template

@app.route('/', methods=['POST']) #Set the route
def my_form_post():
    OldTemp = "Cruddy Python Variable"
    text = request.form['text'] #Get info from First page
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + text #Download the json

    while True:
	response = urllib.urlopen(url) #Download Json
        data = json.loads(response.read()) #Parse json
    	while OldTemp != data['main']['temp'] or OldWeather != data['weather'][0]['description']:
    		response = urllib.urlopen(url) #Download Json
    		data = json.loads(response.read()) #Parse json
    		print("Current Weather in " + text + " " + data['weather'][0]['description']) #Debug infomation
    		print("Temp: " + str(data['main']['temp'])) #Print temp 
		OldTemp = data['main']['temp']
		OldWeather = data['weather'][0]['description']
		if data['weather'][0]['description'].find('rain') > 0:
			WindowControl.Close()
		elif data['main']['temp'] >= 298.15:
			WindowControl.Open()

if __name__ == '__main__':
    app.debug = True #Uncomment to enable debugging
    app.run() #Run the Server