import requests
import pandas as pd
import json
from io import StringIO
from http import HTTPStatus

class Download:

    @staticmethod
    def to_data(url: str):
        try:
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK.value:
                csv_content = StringIO(response.text)
                data = pd.read_csv(csv_content, delimiter = ';')
                return json.loads(data.to_json(orient = 'records'))
            else:
                print(f"Fail to download CSV. Status: { response.status_code }")
        except ConnectionError as e:
            print(f'Fail to connect: {e}')
