from adafruit_pcd8544 import PCD8544
from digitalio import DigitalInOut
import digitalio
import board
import busio
import time

from lcd.app import WeatherDataMenu


class LcdApp:
    display: PCD8544
    terminate_button: DigitalInOut
    weather_data_menu: WeatherDataMenu

    def __init__(self):
        self.display = self.__init_display()
        self.__init_buttons()
        self.weather_data_menu = WeatherDataMenu.WeatherDataMenu()

    def __init_display(self) -> PCD8544:
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        dc = digitalio.DigitalInOut(board.PC4)  # data/command
        cs = digitalio.DigitalInOut(board.PC3)  # Chip select
        reset = digitalio.DigitalInOut(board.PC7)  # reset

        display = PCD8544(spi, dc, cs, reset)
        display.bias = 4
        display.contrast = 60

        return display

    def __init_buttons(self):
        self.terminate_button = digitalio.DigitalInOut(board.PA12)
        self.terminate_button.switch_to_input(pull=digitalio.Pull.UP)

    def __loop_handler(self):
        self.weather_data_menu.display_menu(self.display, 10, 20, 30)

    def main_loop(self) -> None:
        while True:
            self.display.fill(0)
            if not self.terminate_button.value:
                break
            self.__loop_handler()
            self.display.show()
            time.sleep(0.01)
