from apscheduler.schedulers.background import BackgroundScheduler
from adafruit_pcd8544 import PCD8544
from digitalio import DigitalInOut
import digitalio
import board
import busio
import time

from app.menu.WeatherDataMenu import WeatherDataMenu
from app.service.WeatherDataStoreService import WeatherDataStoreService


class LcdApp:
    display: PCD8544
    terminate_button: DigitalInOut
    weather_data_menu: WeatherDataMenu
    weather_data_store_service: WeatherDataStoreService

    def __init__(self):
        self.display = self.__init_display()
        self.__init_buttons()
        self.weather_data_menu = WeatherDataMenu(self.display, "Current data")
        self.weather_data_store_service = WeatherDataStoreService()
        self.__init_scheduler_and_tasks()

    def __init_scheduler_and_tasks(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.weather_data_store_service.get_and_store_measurement, 'interval', seconds=1)
        scheduler.add_job(self.weather_data_store_service.calculate_average_and_save, 'interval', seconds=5)
        scheduler.start()

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
        self.terminate_button = digitalio.DigitalInOut(board.PD14)
        self.terminate_button.switch_to_input(pull=digitalio.Pull.UP)

    def __loop_handler(self):
        self.weather_data_menu.show()

    def __end_execution(self):
        self.display.fill(0)
        self.display.show()

    def main_loop(self) -> None:
        while True:
            if not self.terminate_button.value:
                self.__end_execution()
                break

            self.__loop_handler()
            time.sleep(0.1)
