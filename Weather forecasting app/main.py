from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Weather App")
root.geometry("900x445")
# # Add image file
# bg = PhotoImage(file="image/bg.png")

# # Show image using label
# labelbg = Label(root, image=bg)
# labelbg.place(x=0, y=0)
root.configure(bg="#57adff")
root.resizable(False, False)


def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    print((location.latitude, location.longitude))
    long_lat.config(
        text=f"{round(location.latitude,4)} °N,{round(location.longitude,4)} °E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # weather
    # api key : 0643ece15134962619ef22cef25833a7
    api = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location.latitude)+"&lon=" + str(
        location.longitude)+"&units=metric&exclude=hourly&appid=0643ece15134962619ef22cef25833a7"
    json_data = requests.get(api).json()
    print(json_data)

    # current
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind_speed = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    print(temp)
    print(humidity)
    print(pressure)
    print(wind_speed)
    print(description)

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind_speed, "m/s"))
    d.config(text=description)

    # first cell
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    print(firstdayimage)

    img1 = (Image.open(f"img/{firstdayimage}.png"))
    resized_image1 = img1.resize((90, 90))
    photo1 = ImageTk.PhotoImage(resized_image1)
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")

    # second cell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    print(seconddayimage)

    img2 = (Image.open(f"img/{seconddayimage}.png"))
    resized_image2 = img2.resize((70, 70))
    photo2 = ImageTk.PhotoImage(resized_image2)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")

    # third cell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    print(thirddayimage)

    img3 = (Image.open(f"img/{thirddayimage}.png"))
    resized_image3 = img3.resize((70, 70))
    photo3 = ImageTk.PhotoImage(resized_image3)
    thirdimage.config(image=photo2)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")

    # fourth cell
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    print(fourthdayimage)

    img4 = (Image.open(f"img/{fourthdayimage}.png"))
    resized_image4 = img4.resize((70, 70))
    photo4 = ImageTk.PhotoImage(resized_image4)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")

    # fifth cell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    print(fifthdayimage)

    img5 = (Image.open(f"img/{fifthdayimage}.png"))
    resized_image5 = img5.resize((70, 70))
    photo5 = ImageTk.PhotoImage(resized_image5)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")

    # sixth cell
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    print(sixthdayimage)

    img6 = (Image.open(f"img/{sixthdayimage}.png"))
    resized_image6 = img6.resize((70, 70))
    photo6 = ImageTk.PhotoImage(resized_image6)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")

    # seventh cell
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
    print(seventhdayimage)

    img7 = (Image.open(f"img/{seventhdayimage}.png"))
    resized_image7 = img7.resize((70, 70))
    photo7 = ImageTk.PhotoImage(resized_image7)
    sevethimage.config(image=photo7)
    sevethimage.image = photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")

    # days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seveth = first + timedelta(days=6)
    day7.config(text=seveth.strftime("%A"))


# icon
image_icon = PhotoImage(file="image/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="image/rectangle.png")
Label(root, image=Round_box, bg="#57adff").place(x=20, y=90)

# label
label1 = Label(root, text="Temperature", font=(
    "Helvetica", 11, BOLD), fg="white", bg="#203243")
label1.place(x=30, y=100)

label2 = Label(root, text="Humidity", font=(
    "Helvetica", 11, BOLD), fg="white", bg="#203243")
label2.place(x=30, y=120)

label3 = Label(root, text="Pressure", font=(
    "Helvetica", 11, BOLD), fg="white", bg="#203243")
label3.place(x=30, y=140)

label4 = Label(root, text="Wind Speed", font=(
    "Helvetica", 11, BOLD), fg="white", bg="#203243")
label4.place(x=30, y=160)

label5 = Label(root, text="Description", font=(
    "Helvetica", 11, BOLD), fg="white", bg="#203243")
label5.place(x=30, y=180)

# Search box

Search_img = PhotoImage(file="image/searbar.png")
myimage = Label(image=Search_img, bg="#57adff")
myimage.place(x=350, y=110)

weat_img = PhotoImage(file="img/04d.png")
weatherImage = Label(root, image=weat_img, bg="#203243")
weatherImage.place(x=375, y=112)


textfield = tk.Entry(root, justify="center", width=13, font=(
    'poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=420, y=118)
textfield.focus()

searchicon = PhotoImage(file="image\serlogo.png")
myimage_icon = Button(image=searchicon, borderwidth=0,
                      cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=690, y=112)


# bOTTOM bOX

frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# bottom boxes
firstbox = PhotoImage(file="image/rectangle2.png")
secondbox = PhotoImage(file="image/rectangle3.png")

Label(frame, image=firstbox, bg="#212120").place(x=16, y=23)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=23)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=23)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=23)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=23)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=23)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=23)


# clock(here we will place time)
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)


# timezone
timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)


long_lat = Label(root, font=("Helvetica", 13, 'bold'),
                 fg="white", bg="#57adff")
long_lat.place(x=700, y=55)


# data  P  H  T  W  D
t = Label(root, font=(
    'Helvetica', 11, 'bold'), fg='white', bg='#203243')
t.place(x=150, y=100)

h = Label(root, font=(
    'Helvetica', 11, 'bold'), fg='white', bg='#203243')
h.place(x=150, y=120)

p = Label(root, font=(
    'Helvetica', 11, 'bold'), fg='white', bg='#203243')
p.place(x=150, y=140)

w = Label(root, font=(
    'Helvetica', 11, 'bold'), fg='white', bg='#203243')
w.place(x=150, y=160)

d = Label(root, font=(
    'Helvetica', 11, 'bold'), fg='white', bg='#203243')
d.place(x=150, y=180)


# first cell
firstframe = Frame(root, width=270, height=137, bg="#282829")
firstframe.place(x=18, y=290)

day1 = Label(firstframe, font='arial 20 bold', bg="#282829", fg="#fff")
day1.place(x=110, y=5)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=10, y=25)

day1temp = Label(firstframe, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100, y=50)

# second cell
secondframe = Frame(root, width=83, height=138, bg="#282829")
secondframe.place(x=303, y=290)

day2 = Label(secondframe, font='arial 10 bold', bg="#282829", fg="#fff")
day2.place(x=6, y=5)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=7, y=25)

day2temp = Label(secondframe, bg="#282829", fg="#fff", font="arial 10 bold")
day2temp.place(x=5, y=80)

# third cell
thirdframe = Frame(root, width=83, height=138, bg="#282829")
thirdframe.place(x=403, y=290)

day3 = Label(thirdframe, font='arial 10 bold', bg="#282829", fg="#fff")
day3.place(x=7, y=5)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=7, y=25)

day3temp = Label(thirdframe, bg="#282829", fg="#fff", font="arial 10 bold")
day3temp.place(x=5, y=80)


# fourth cell
fourthframe = Frame(root, width=83, height=138, bg="#282829")
fourthframe.place(x=503, y=290)

day4 = Label(fourthframe, font='arial 10 bold', bg="#282829", fg="#fff")
day4.place(x=8, y=5)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=7, y=25)

day4temp = Label(fourthframe, bg="#282829", fg="#fff", font="arial 10 bold")
day4temp.place(x=5, y=80)

# fifth cell
fifthframe = Frame(root, width=83, height=138, bg="#282829")
fifthframe.place(x=603, y=290)


day5 = Label(fifthframe, font='arial 10 bold',  bg="#282829", fg="#fff")
day5.place(x=10, y=5)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=7, y=25)

day5temp = Label(fifthframe, bg="#282829", fg="#fff", font="arial 10 bold")
day5temp.place(x=5, y=80)

# sixth cell
sixthframe = Frame(root, width=83, height=138, bg="#282829")
sixthframe.place(x=703, y=290)

day6 = Label(sixthframe, font='arial 10 bold',  bg="#282829", fg="#fff")
day6.place(x=10, y=5)

sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=7, y=25)

day6temp = Label(sixthframe, bg="#282829", fg="#fff", font="arial 10 bold")
day6temp.place(x=5, y=80)


# seveth cell
sevethframe = Frame(root, width=83, height=138, bg="#282829")
sevethframe.place(x=803, y=290)

day7 = Label(sevethframe, font='arial 10 bold', bg="#282829", fg="#fff")
day7.place(x=10, y=5)

sevethimage = Label(sevethframe, bg="#282829")
sevethimage.place(x=7, y=25)

day7temp = Label(sevethframe, bg="#282829", fg="#fff", font="arial 10 bold")
day7temp.place(x=5, y=80)


root.mainloop()
