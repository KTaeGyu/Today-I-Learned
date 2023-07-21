from pprint import pprint
import requests

lat = 37.56
lon = 126.97
API_key = '947888ee29147f29548db7514f4b220c'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

response = requests.get(url).json()

temp = response['main']['temp']

print(f'캘빈 온도 : {temp}K')
print(f'섭씨 온도 : {temp-273.15:.2f}\u2103')