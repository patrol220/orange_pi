from adafruit_pcd8544 import PCD8544
from abc import ABC, abstractmethod


class MenuAbstract(ABC):
    display: PCD8544
    title: str

    def __init__(self, display: PCD8544, title: str = ""):
        self.display = display
        self.title = title

    def show(self):
        self.display.fill(0)
        if self.title != "":
            self.__draw_title()

        self.show_menu()
        self.display.show()

    @abstractmethod
    def show_menu(self):
        ...

    def __draw_title(self):
        self.display.fill_rect(0, 0, 84, 9, 1)
        self.display.text(self.title, 1, 1, 0)

