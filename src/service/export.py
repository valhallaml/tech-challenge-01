import json
from service.download import Download

class Export:

    @staticmethod
    def get_export(product_id: int = None):
        data = Download.get_file('ExpVinho.csv')
        if product_id is not None:
            data = data[data['id'] == product_id]
            del data['id']
        return json.loads(data.to_json(orient = 'records'))
