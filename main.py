
from weather4py import WeatherMan
import easygui



weatherLocation = str(input("What is the location you would like to get the weather for?: "))

# takes an input of metric(C)/imperial(F)
WeatherMan("owo").set_measurement("metric")

print("Weather:")
# to get the weather of a location
print(WeatherMan(weatherLocation).weather)

print("Tempurature (°C):")
# to get the temperature of a location
print(WeatherMan(weatherLocation).temperature)


print("Humidity:")
# to get the humidity of a location
print(WeatherMan(weatherLocation).humidity)

# to reobtain infromation about a location.
WeatherMan("owo").obtain_information()




file_save_location = easygui.filesavebox()
f = open(file_save_location,"a")


f.write("Weather: " + str(WeatherMan(weatherLocation).weather))
f.write(" \n")
f.write("Tempurature (°C): " + str(WeatherMan(weatherLocation).temperature))
f.write(" \n")
f.write("Humidity: " + str(WeatherMan(weatherLocation).humidity))


f.close()