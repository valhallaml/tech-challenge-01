import json
from service.download import Download


class Production:

    @staticmethod
    def get_production(product_id: int = None):
        data = Download.get_file('Producao.csv')
        if product_id is not None:
            data = data[data['id'] == product_id]
            del data['id']
        return json.loads(data.to_json(orient = 'records'))
