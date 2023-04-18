from adafruit_pcd8544 import PCD8544


class WeatherDataMenu:
    def display_menu(
            self,
            display: PCD8544,
            temperature: float,
            humidity: float,
            pressure: float
    ):
        display.text("Temp: " + str(temperature) + " C", 0, 0, 1)
        display.text("Hum: " + str(humidity) + "%", 0, 10, 1)
        display.text("hPa: " + str(pressure), 0, 20, 1)
