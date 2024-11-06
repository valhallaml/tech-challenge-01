import json
from service.download import Download

class Processes:

    @staticmethod
    def get_processes(product_id: int = None):
        data = Download.get_file('ProcessaViniferas.csv')
        if product_id is not None:
            data = data[data['id'] == product_id]
            del data['id']
        return json.loads(data.to_json(orient = 'records'))
