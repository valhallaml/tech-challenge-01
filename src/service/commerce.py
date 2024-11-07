import json
from service.download import Download

class Commerce:

    @staticmethod
    def get_commerce(product_id: int = None):
        data = Download.get_file('Comercio.csv')
        if product_id is not None:
            data = data[data['id'] == product_id]
            del data['id']
        return json.loads(data.to_json(orient = 'records'))
