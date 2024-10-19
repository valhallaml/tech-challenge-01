import requests
import pandas as pd
from io import StringIO

class Download:

    @staticmethod
    def to_data(url: str):
        response = requests.get(url)
        if response.status_code == 200:
            csv_content = StringIO(response.text)
            return pd.read_csv(csv_content)
        else:
            print(f"Fail to download CSV. Status: {response.status_code}")
