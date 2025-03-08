import tkinter as tk
from tkinter import messagebox
import requests

window = tk.Tk()
window.title("nina Weather app")
window.minsize(400, 300)
window.maxsize(400, 300)  
window.resizable(False, False)

city_var = tk.StringVar()
city_label = tk.StringVar()
situationdata_lable = tk.StringVar()
templabledata_lable = tk.StringVar()
maxtemp_data = tk.StringVar()
mintemp_data = tk.StringVar()
cold_message = tk.StringVar()  

def widgets():
    city_ename = tk.Label(window, text="اسم شهر:")
    city_ename.grid(row=0, column=0)

    city_entry = tk.Entry(window, width=30, textvariable=city_var)
    city_entry.grid(row=0, column=1)

    city_search = tk.Button(window, text="جستجو", bg="orange", command=search)
    city_search.grid(row=0, column=2)

    city_labler = tk.Label(window, text="نام شهر:")
    city_labler.grid(row=1, column=0, pady=30)

    city_lable_data = tk.Label(text="----", textvariable=city_label)
    city_lable_data.grid(row=1, column=1)

    situation_lable = tk.Label(window, text="وضعیت:")
    situation_lable.grid(row=2, column=0)

    situation_lable_data = tk.Label(window, text="----", textvariable=situationdata_lable)
    situation_lable_data.grid(row=2, column=1)

    temp_lable = tk.Label(window, text="دما:")
    temp_lable.grid(row=3, column=0, pady=30)

    temp_lable_data = tk.Label(window, text="----", textvariable=templabledata_lable)
    temp_lable_data.grid(row=3, column=1)

    cold_message_label = tk.Label(window, textvariable=cold_message, fg="red")
    cold_message_label.grid(row=3, column=3)

    maxtemp_lable = tk.Label(window, text="بیشترین دما:")
    maxtemp_lable.grid(row=4, column=0)

    maxtemp_lable_data = tk.Label(window, text="----", textvariable=maxtemp_data)
    maxtemp_lable_data.grid(row=4, column=1)

    mintemp_lable = tk.Label(window, text="کمترین دما:")
    mintemp_lable.grid(row=5, column=0, pady=30)

    mintemp_lable_data = tk.Label(window, text="---", textvariable=mintemp_data)
    mintemp_lable_data.grid(row=5, column=1, pady=30)

def search():
    city = city_var.get()    
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    appid = "dd37b7000f35f392a6129b57fc14107d"
    response = requests.get(url.format(city, appid))
    
    data = response.json()
    city_label.set(data["name"])
    situationdata_lable.set(data["weather"][0]["main"])
    temp = data["main"]["temp"]  
    templabledata_lable.set(f"{temp} °C")
    maxtemp_data.set(f"{data['main']['temp_max']}°C")
    mintemp_data.set(f"{data['main']['temp_min']}°C")
    
    if 0 <= temp <= 10:
        cold_message.set("سرده لامصب!")
    elif 11<= temp <=15:
        cold_message.set("هوا عالیه")
    elif 16<= temp <=20:
        cold_message.set("بد نی همچینم")
    elif 21<= temp <=25:
        cold_message.set("یه نوشیدنی سر میچسبه")
    elif 26<= temp <=30:
        cold_message.set("اینجا جهنمه")
    elif 31<= temp <=35:
        cold_message.set("داریم ذوب میشیم!")

    


widgets()
window.mainloop()