from adafruit_bmp280 import Adafruit_BMP280_I2C
from adafruit_ahtx0 import AHTx0
import board


class WeatherDataProvider:
    weather_module_bmp280: Adafruit_BMP280_I2C
    weather_module_aht20: AHTx0

    def __init__(self):
        self.weather_module_bmp280 = self.__init_weather_module_bmp280()
        self.weather_module_aht20 = self.__init_weather_module_aht20()

    def __init_weather_module_bmp280(self) -> Adafruit_BMP280_I2C:
        i2c = board.I2C()
        bmp280 = Adafruit_BMP280_I2C(i2c)

        return bmp280

    def __init_weather_module_aht20(self) -> AHTx0:
        i2c = board.I2C()
        aht20 = AHTx0(i2c)

        return aht20

    def get_temperature(self) -> float:
        return self.weather_module_bmp280.temperature

    def get_humidity(self) -> int:
        return self.weather_module_aht20.relative_humidity

    def get_pressure(self) -> float:
        return self.weather_module_bmp280.pressure
