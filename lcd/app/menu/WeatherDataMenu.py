from adafruit_pcd8544 import PCD8544
from ..provider.WeatherDataProvider import WeatherDataProvider
from ..menu.MenuAbstract import MenuAbstract


class WeatherDataMenu(MenuAbstract):
    weather_data_provider: WeatherDataProvider

    def __init__(self, display, title):
        self.weather_data_provider = WeatherDataProvider()
        super().__init__(display, title)

    def show_menu(self):
        self.display.text("Temp: " + self.__format_numeric_value_to_string(self.weather_data_provider.get_temperature()) + " C", 0, 10, 1)
        self.display.text("Hum: " + self.__format_numeric_value_to_string(self.weather_data_provider.get_humidity()) + "%", 0, 20, 1)
        self.display.text("hPa: " + self.__format_numeric_value_to_string(self.weather_data_provider.get_pressure()), 0, 30, 1)

    def __format_numeric_value_to_string(self, value: float) -> str:
        return str(round(value, 1))
