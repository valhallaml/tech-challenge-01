import os
import requests
import pandas as pd

from io import StringIO
from diskcache import Cache
from requests.exceptions import ConnectionError

class Download:

    _CACHE_DURATION = 3600 # 1 hour
    _BASE_REMOTE_URL = 'http://vitibrasil.cnpuv.embrapa.br/download/'
    _BASE_LOCAL_URL = 'embrapa/'

    _cache = Cache()

    @staticmethod
    def __download_remote_file(filename: str):
        """Download remote file and create cache."""
        try:
            response = requests.get(f'{Download._BASE_REMOTE_URL}{filename}', timeout=5)
            response.raise_for_status()
            response.encoding = 'UTF-8'
            data = response.text
            print(f'Downloaded {filename} from remote')
            Download._cache.set(filename, data, Download._CACHE_DURATION)
            print(f'Created {filename} cache')
            return data
        except ConnectionError as e:
            print(f'Error on connecting: {e}')
        except Exception as e:
            print(f'Unknown error on download: {e}')

    @staticmethod
    def __get_file_cache(filename: str):
        """Get file from cache if exists."""
        cached_data = Download._cache.get(filename)

        if cached_data:
            print(f"{filename} found on cache.")
            return cached_data

    @staticmethod
    def __get_file_local(filename: str):
        """Get file from local disk"""
        local_file_path = os.path.join(Download._BASE_LOCAL_URL, filename)

        if os.path.exists(local_file_path):
            with open(local_file_path, 'r', encoding='UTF-8') as file:
                csv_data = file.read()
            print(f'{filename} file load from local.')

            # save on cache
            Download._cache.set(filename, csv_data, expire=Download._CACHE_DURATION)
            return csv_data
        else:
            print(f'File {filename} not found.')

    @staticmethod
    def _get_data(filename: str):
        """Get file content."""
        # 1. try to find the file in the cache
        data = Download.__get_file_cache(filename)
        if data is not None:
            return data

        # 2. if not found, download from remote
        data = Download.__download_remote_file(filename)
        if data is not None:
            return data

        # 3. if download fails, try load from local
        data = Download.__get_file_local(filename)
        if data is not None:
            return data

        raise Exception(f'Could not get file {filename} from any source.')

    @staticmethod
    def get_file(filename: str):
        """Get file from name."""
        data = Download._get_data(filename)
        csv_content = StringIO(data)
        return pd.read_csv(csv_content, delimiter=';', encoding='UTF-8')
