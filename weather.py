from pyowm import OWM
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
owm = OWM('ea826b6d56499a2fd23041e97e711d8c')
owm.supported_languages
config_dict['language'] = 'ru'
mgr = owm.weather_manager()
# Search for current weather in Sevastopol (Russia) and get details
place = input("В каком городе/стране?: ")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]
cld = w.detailed_status

print("В городе " + place + " сейчас: " + cld)
print( "Температура сейчас в районе: " + str(temp) + " градусов")

if (temp < 10):
    print("Холодно")
if (temp < 20):
    print("Прохладно")
if (temp > 20):
    print("Тепло")    
