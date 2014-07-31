import urllib, json
url = "http://api.openweathermap.org/data/2.5/weather?q=London"
response = urllib.urlopen(url)
data = json.loads(response.read())
print(data['weather'][0]['description'])
