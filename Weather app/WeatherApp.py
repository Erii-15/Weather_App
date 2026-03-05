from tkinter import * #for ui for application
import geocoder # module installed to get location
from config import apiKey #my personal api key
import requests #library that lets your program talk to websites and APIs
from PIL import Image, ImageTk # for handling of pictures

app=Tk()
app.geometry('500x500') #size of window

MyLocation=geocoder.ip('me') #getting device location
cityName=MyLocation.city
city_label=Label(app,text=cityName,font=('bold Arial',20))
city_label.pack() #actually adds to UI

#actually talkin with the api
APIKey=apiKey
Url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
responce=requests.get(Url.format(cityName,APIKey))
# print("Status code:", responce.status_code)
# print("Raw text:", responce.text)
data=responce.json()
if data:
    temp=data["main"]["temp"]   
    decription=data["weather"][0]["description"]
    sunrise_unix=data["sys"]["sunrise"]
    sunset_unix=data["sys"]["sunset"]
    weather_main=data["weather"][0]["main"]
else:
    error_Label=Label(app,text="Error getting and displaying weather",font=('bold Arial',20),bg="red")
    error_Label.pack()

weather_image = {
    "Clouds": "Images/Cloudy.png",
    "Rain": "Images/Rain.png",
    "Drizzle": "Images/Rain.png",
    "Snow": "Images/Snowy.png",
    "Clear": "Images/Sunny.png",
    "Thunderstorm": "Images/Thunder.png",
    "Mist": "Images/Cloudy.png",
    "Fog": "Images/Cloudy.png"
}

if weather_main in weather_image: #dont fully understand
    # Open the image file that matches the current weather
    img = Image.open(weather_image[weather_main])
    # Convert the PIL image into a format that Tkinter can display
    photo = ImageTk.PhotoImage(img)
    # Create a Tkinter Label widget that will display the image
    weather_pic = Label(app, image=photo)
    # This prevents Python's garbage collector from deleting the image
    weather_pic.image = photo
    # Add the label (with the image) to the window so it becomes visible
    weather_pic.pack()

tempCel=temp - 273.15
tempCelText = f"{tempCel:.2f}°C"  # format to 2 decimal places   
tempCel_label=Label(app,text=tempCelText,font=('bold Arial',20))
tempCel_label.pack()

tempFah=9/5 * (tempCel) + 32
tempFahText=f"{tempFah:.2f}°F"
tempFah_label=Label(app,text=tempFahText,font=("bold Arial",20))
tempFah_label.pack()

decrip_label=Label(app,text=decription,font=("bold Arial",20))
decrip_label.pack()

# weather-main- for the main weather e.g rain
# make a list of the pic and see when the pic name matches the weather main

app.mainloop()