import json  
import turtle
import urllib.request 
import time 
import webbrowser 
import geocoder

"""codes: geeksforgeeks"""
  
url = "http://api.open-notify.org/astros.json" 
response = urllib.request.urlopen(url) 
result = json.loads(response.read())
print(result) # Get astronouts info

file = open("iss.txt", "w") 
file.write(
  "There are currently " + str(result["number"]) + 
  " astronauts on the ISS: \n\n")
  
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

print(people)

"""Use geocoder.ip(‘me’) to know your current location in terms of latitude and longitude 
and after that using write the data in the file
and then close the file using the file.close() function."""

# print long and lat
g = geocoder.ip('me') 
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

time.sleep(5)

# Setting Up The World Map

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
# load the world map image
screen.bgpic("images\map.gif")
screen.register_shape("images\iss.gif")
iss = turtle.Turtle()
iss.shape("images\iss.gif")
iss.setheading(45)
iss.penup()


# load the current status of the ISS in real-time
url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
  
# Extract the ISS location
location = result["iss_position"]
lat = location['latitude']
lon = location['longitude']
  
# Output lon and lat to the terminal in the 
# float format
lat = float(lat)
lon = float(lon)
print("\nLatitude: " + str(lat))
print("\nLongitude: " + str(lon))

# Update the position of ISS every 5 seconds by refreshing the latitude and longitude value from API.


# Update the ISS location on the map
iss.goto(lon, lat)
  
# Refresh each 5 seconds
time.sleep(7)

