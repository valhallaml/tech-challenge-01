# http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv
# http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv
# http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv
# http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv
# http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv

from download import Download

class Embrapa:

    # _base_url = 'http://vitibrasil.cnpuv.embrapa.br/download'
    _base_url = 'http://embrapa'

    @staticmethod
    def get_production():
        return Download.to_data(Embrapa._base_url + '/Producao.csv')
