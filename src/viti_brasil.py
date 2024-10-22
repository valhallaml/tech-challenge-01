import json
from download import Download

# http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv
# http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv
# http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv
# http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv
# http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv

class Embrapa:

    _base_url = 'http://vitibrasil.cnpuv.embrapa.br/download'
    # _base_url = 'http://embrapa'

    @staticmethod
    def get_production(product_id: int = None):
        data = Download.to_data(Embrapa._base_url + '/Producao.csv')
        if product_id is not None:
            data = data[data['id'] == product_id]
            del data['id']
        return json.loads(data.to_json(orient = 'records'))
