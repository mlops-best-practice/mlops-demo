import pandas as pd


class DataLoader:
    def __init__(self, location_path):
        self.location_path = location_path

    def load_data(self):
        df = pd.read_csv(self.location_path)
        return df


    
