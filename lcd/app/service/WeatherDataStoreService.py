from ..provider.WeatherDataProvider import WeatherDataProvider


class WeatherDataStoreService:
    measurements: []
    weather_data_provider: WeatherDataProvider

    def __init__(self):
        self.measurements = []
        self.weather_data_provider = WeatherDataProvider()

    def get_and_store_measurement(self):
        measurement = [0, 0, 0]
        measurement[0] = self.weather_data_provider.get_temperature()
        measurement[1] = self.weather_data_provider.get_humidity()
        measurement[2] = self.weather_data_provider.get_pressure()
        self.measurements.append(measurement)

    def calculate_average_and_save(self):
        average_measurements = []

        for measurement in (zip(*self.measurements)):
            average_measurements.append(sum(measurement) / len(measurement))

        #todo save to database
