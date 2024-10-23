import requests
import pandas as pd
from io import StringIO
from http import HTTPStatus

class Download:

    @staticmethod
    def to_data(url: str):
        try:
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK.value:
                response.encoding = 'UTF-8'
                csv_content = StringIO(response.text)
                return pd.read_csv(csv_content, delimiter = ';', encoding = 'UTF-8')
            else:
                print(f"Fail to download CSV. Status: { response.status_code }")
        except ConnectionError as e:
            print(f'Fail to connect: {e}')
