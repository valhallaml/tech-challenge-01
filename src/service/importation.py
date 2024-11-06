import json
from service.download import Download

class Importation:

    @staticmethod
    def get_importation(importantion_id: int = None):
        data = Download.get_file('ImpVinhos.csv')
        if importantion_id is not None:
            data = data[data['Id'] == importantion_id]
            del data['Id']
        return json.loads(data.to_json(orient = 'records'))
