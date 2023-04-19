from adafruit_pcd8544 import PCD8544
from ..provider.WeatherDataProvider import WeatherDataProvider


class WeatherDataMenu:
    weather_data_provider: WeatherDataProvider

    def __init__(self):
        self.weather_data_provider = WeatherDataProvider()

    def display_menu(
            self,
            display: PCD8544
    ):
        display.text("Temp: " + str(self.weather_data_provider.get_temperature()) + " C", 0, 0, 1)
        display.text("Hum: " + str(self.weather_data_provider.get_humidity()) + "%", 0, 10, 1)
        display.text("hPa: " + str(self.weather_data_provider.get_pressure()), 0, 20, 1)
