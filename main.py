from datetime import datetime
import time
import csv
import requests as req
def weather(city_list,temp_units):
    value_list=[]

    for city in city_list:
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=298318be08eef2fada79a0583ffd1fad&units={temp_units}'

        try:
            r=req.get(url)
            if r.status_code>200:
                print(f"Can't find your city '{city}', try another one!")
        except req.exceptions.RequestException:
            print('Some problems with server connecting,please try later!')
        else:
            respond_dict=r.json()
            now = datetime.utcnow()
            current_time = now.strftime("%H:%M:%S")
            milliseconds = int(round(time.time() * 1000))
            try:
                formated_dict=respond_dict['name'],respond_dict['id'],milliseconds,current_time, respond_dict['main']['temp'],respond_dict['weather'][0]['description'],respond_dict['main']['pressure'],respond_dict['wind']['speed']
            except:
                pass
            else:
                value_list.append(formated_dict)
                print(value_list)
        headers=['Name','Id','Milliseconds','Current time','Temperature','Visibility','Pressure','Wind_speed']
        readable_file = 'weather_data.csv'
        with open(readable_file, 'w') as f:
            write=csv.writer(f)
            write.writerow(headers)
            write.writerows(value_list)

citys_list=['zhytomyr','madrid','dubai']
weather(citys_list,'metric')