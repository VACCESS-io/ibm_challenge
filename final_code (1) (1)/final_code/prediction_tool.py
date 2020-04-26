from input_data_set import input_data
from math import log2, ceil
from enum import Enum, auto
from matplotlib import pyplot as plt
import csv
import datetime
from dateutil.relativedelta import relativedelta
import re


class Status(Enum):
    UNDER_CONTROL = auto()
    ABOVE_THRESHOULD = auto()
    RED_ALERT = auto()


class PredictionTool:

    def __init__(self):
        self.extendend_capability = None
        self.real_capability = None
        self.fields = list()

    def generate_csv_file(self, state_name: str, csv_data):
        with open(f'{state_name}_prediction_data.csv', 'w', encoding='utf8', newline='') as outfile:
            fc = csv.DictWriter(outfile, fieldnames=csv_data[0].keys())
            fc.writeheader()
            fc.writerows(csv_data)

    def set_field_names(self, first_row):
        for key, value in first_row.items():
            if isinstance(value, list):
                value = value[0]
            else:
                self.fields.append(key)
            if isinstance(value, dict):
                self.set_field_names(value)

    def process_state_data(self):
        for state_data in input_data:
            self.process_county_data(state_data)

    def process_county_data(self, state_data: list):
        predictions = list()
        for data in state_data.county_data:
            self.set_current_county_capability(data)
            predictions.extend(self.generate_daily_prediction(data))
        self.generate_csv_file(state_data.name, predictions)

    @staticmethod
    def calculate_date(delta: int = 0):
        #today = datetime.datetime.today()
        start_date = datetime.date(2020, 4, 19)
        next_date = start_date + relativedelta(days=delta)
        return next_date.strftime("%Y-%m-%d")

    def set_current_county_capability(self, data):
        self.real_capability = data.num_doctor * 5
        self.extendend_capability = data.num_doctor * 8

    def generate_past_prediction(self, data):
        previous_day_count = 1
        predictions = list()
        infection_since = round(log2(data.infected_population))
        for count in range(infection_since):
            next_day_count = ((2/data.doubling_rate_days) * previous_day_count)
            if next_day_count >= data.infected_population:
                break
            status = self.get_status(next_day_count)
            predictions.append(dict(affected_percent=(data.infected_population/data.population)*100, status=status))
        return predictions

    def generate_daily_prediction(self, data):
        red_alert_count = 0
        prediction = list()
        current_status = self.get_status(data.infected_population)
        red_alert_count += 1 if current_status == Status.RED_ALERT else 0
        prediction.append(dict(name=data.name[0], date=self.calculate_date(), count=data.infected_population, status=current_status))
        #prediction.append(dict(affected_percent=(data.infected_population/data.population)*100, status=current_status))
        previous_day_count = data.infected_population
        counts = list()
        counts.append(data.infected_population)
        day_count = 1
        while red_alert_count <= 10:
            next_day_count = previous_day_count + ((2/data.doubling_rate_days) * previous_day_count)
            next_day_status = self.get_status(next_day_count)
            red_alert_count += 1 if next_day_status == Status.RED_ALERT else 0
            affected_percent = (next_day_count/data.population) * 100
            prediction.append(dict(name=data.name[0], date=self.calculate_date(delta=day_count), count=next_day_count, status=next_day_status))
            counts.append(next_day_count)
            previous_day_count = next_day_count
            day_count += 1
        plt.plot(counts)
        return prediction

    def get_status(self, infected_count):
        if infected_count <= self.real_capability:
            return Status.UNDER_CONTROL
        elif (infected_count >= self.real_capability) and (infected_count < self.extendend_capability):
            return Status.ABOVE_THRESHOULD
        else:
            return Status.RED_ALERT


PredictionTool().process_state_data()