import pandas as pd
import numpy as np

class DataAccessor:
    # Class to access the data and pre-process it
    
    def __init__(self):
        pass

    def get_heart_data(self, path):
        data = pd.read_csv(path)
        values = data[data['source'] == 'heart_rate']["values"]
        list_array = np.array([eval(item) for item in values])
        heart_data = np.array([float(item[0]) for item in list_array])
        
        return heart_data
    
    def get_steps_data(self, path):
        data = pd.read_csv(path)
        values = data[data['source'] == 'steps']["values"]
        list_array = np.array([eval(item) for item in values])
        steps_data = np.array([float(item[0]) for item in list_array])
        
        return steps_data
    
    def get_sleep_duration(self, path):
        data = pd.read_csv(path)
        values = data[data['source'] == 'sleep_duration']["values"]
        list_array = np.array([eval(item) for item in values])
        sleep_data = np.array([float(item[0]) for item in list_array])
        
        return sleep_data



