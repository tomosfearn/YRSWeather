#Used for starting the flask server
from flask import Flask #Import flask mains
from flask import request #Import flask requests
from flask import render_template #Import flask render templates
import json, urllib #import api modules
import time #Imporing time in darlek voice
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html") #Set render template

@app.route('/', methods=['POST'])
def my_form_post():
    openwindow_at = float(request.form['open']) #When it reached ? open window
    if request.form['scale'] == "kelvin": #Change figures
	print("Do nothing")
    elif request.form['scale'] == "celcius":
	openwindow_at = openwindow_at + 273 #celcius to kelvin
    elif request.form['scale'] == "fah": #Fah to kelvin
	openwindow_at = (openwindow_at + 459.67) * 5 / 9  #F to kelvin
    text = request.form['text'] #Get info from First page
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + text #Download the json
    response = urllib.urlopen(url) #Download Json
    data = json.loads(response.read()) #Parse json
    print("Current Weather in " + text + " " + data['weather'][0]['description']) #Debug infomation
    print("Temp: " + str(data['main']['temp'])) #Print temp 
    if data['weather'][0]['description'].find("rain") >= 0: #Check The weather
	return "Shutting your window" #Send to page
	#Close the window(Tom's job)
    else:
	if data['main']['temp'] >= openwindow_at:
		return "Opening your window" #Send to page
    		#open the window (Tom's job)
if __name__ == '__main__':
    #app.debug = True #Uncomment to enable debugging
    app.run()
