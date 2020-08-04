import pprint
import requests
from dateutil.parser import parser

#https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&mode=xml&appid=439d4b804bc8187953eb36d2a8c26a02
# api_key = 89edf381b7ee15db0d8e96ff8708033d
class YahooWeatherForecast:

	def __init__(self):
		self._city_cache = {}


	def get(self, city):
		if city in self._city_cache:
			return self._city_cache[city]

		url = f"pro.openweathermap.org/data/2.5/forecast/hourly?q={city},us&mode=json&appid={api_key}"
		print("sending HHTP request")
		data = requests.get(url).json()
		forecast_data = data[]
		forecast = []

		# обработка джейсоновского файла для получения прогноза погоды
		# for day_data in forecast_data:
		# 	forecast.append()

		self._city_cache[city] = forecast

		return forecast


class CityInfo:

	def __init__(self, city, weather_forecast=None):
		self.city = city
		self._weather_forecast = weather_forecast or YahooWeatherForecast()



	def weather_forecast(self):
		return self._weather_forecast.get(self.city)




def _main():
	weather_forecast = YahooWeatherForecast()

	for i in range(5):
		city_info = CityInfo("Moscow", weather_forecast=weather_forecast)
		city_info.weather_forecast()


	city_info = CityInfo("Moscow")
	forecast = city_info.weather_forecast()
	pprint.pprint(forecast)

if __name__ == "__main__":
	_main()
