from flask import Flask
from flask import request
from flask import render_template
import json, urllib
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + text
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    if data['weather'][0]['description'].find("Rain") >= 0:
	return "Shut your window"
    else:
	return "everything is fine"
    
if __name__ == '__main__':
    app.debug = True
    app.run()
