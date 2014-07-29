#Used for starting the flask server
from flask import Flask
from flask import request
from flask import render_template
import json, urllib
import time
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    openwindow_at = int(request.form['open'])
    if request.form['scale'] == "kelvin":
	print("Do nothing")
    elif request.form['scale'] == "celcius":
	openwindow_at = openwindow_at + 273 #celcius to kelvin
    elif request.form['scale'] == "fah":
	openwindow_at = (openwindow_at + 459.67) * 5 / 9  #F to kelvin
    text = request.form['text']
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + text
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print("Current Weather in " + text + " " + data['weather'][0]['description'])
    while True:
    	if data['weather'][0]['description'].find("rain") >= 0:
		return "Shutting your window"
		#Close the window(Tom's job)
    	else:
		if data['main']['temp'] >= 200:
			return "Opening your window"
    			#open the window (Tom's job)
if __name__ == '__main__':
    app.debug = True
    app.run()
