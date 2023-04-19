from adafruit_bmp280 import Adafruit_BMP280_I2C
import board


class WeatherDataProvider:
    weather_module: Adafruit_BMP280_I2C

    def __init__(self):
        self.weather_module = self.__init_weather_module()

    def __init_weather_module(self) -> Adafruit_BMP280_I2C:
        i2c = board.I2C()
        bmp280 = Adafruit_BMP280_I2C(i2c)

        return bmp280

    def get_temperature(self):
        return self.weather_module.temperature

    def get_humidity(self):
        return 3

    def get_pressure(self):
        return self.weather_module.pressure
