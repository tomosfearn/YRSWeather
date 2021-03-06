#Used for starting the flask server
from flask import Flask #Import flask mains
from flask import request #Import flask requests
from flask import render_template #Import flask render templates
from flask import url_for
import json, urllib #import api modules
import time #Imporing time in darlek voice
import WindowControl
app = Flask(__name__, static_url_path="/static/css")
@app.route('/')
def my_form():
    return render_template("my-form.html") #Set render template

@app.route('/', methods=['POST']) #Set the route
def my_form_post():
    openwindow_at = float(request.form['open']) #When it reached ? open window
    if request.form['scale'] == "kelvin": #Change figures
	print("Do nothing") #Debug info
    elif request.form['scale'] == "celcius":
	openwindow_at = openwindow_at + int(273.15) #celcius to kelvin
    elif request.form['scale'] == "fah": #Fah to kelvin
	openwindow_at = (openwindow_at + 459.67) * 5 / 9  #F to kelvin
    text = request.form['text'] #Get info from First page
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + text #Download the json
    response = urllib.urlopen(url) #Download Json
    data = json.loads(response.read()) #Parse json
    print("Current Weather in " + text + " " + data['weather'][0]['description']) #Debug infomation
    print("Temp: " + str(data['main']['temp'])) #Print temp 

    if data['weather'][0]['description'].find("rain") >= 0: #Check The weather
	WindowControl.Close()
	return "Shutting your window"
    elif float(data['main']['temp']) >= openwindow_at:
	WindowControl.Open()
	return "Opening your window And turning on fans"
    elif data['main']['temp'] < openwindow_at:
	WindowControl.Close()
	return "Shutting Your Window And turning off fans"
if __name__ == '__main__':
    #app.debug = True #Uncomment to enable debugging
    app.run(host='0.0.0.0') #Run the Server
