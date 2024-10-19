import requests
import pandas as pd
import json
from io import StringIO

class Download:

    @staticmethod
    def to_data(url: str):
        response = requests.get(url)
        if response.status_code == 200:
            csv_content = StringIO(response.text)
            data = pd.read_csv(csv_content, delimiter=';')
            return json.loads(data.to_json(orient='records'))
        else:
            print(f"Fail to download CSV. Status: {response.status_code}")
