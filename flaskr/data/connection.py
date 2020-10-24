import json
from datetime import datetime


def get_all_data(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
            return data
    except:
        return "Error, could not find JSON"


def get_wind_data(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
            return data[1]["wind"]
    except:
        return "Error, could not find JSON"


def time_stamp_to_date(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object
