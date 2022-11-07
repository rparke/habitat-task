import requests
import pandas as pd
from io import StringIO
import logging


class DataSource:
    """
    DataSource Object: for Database Consumer to Use
    """

    def __init__(self):
        pass

    def _get_data_from_request(self, uri):
        logging.info(f"Sending GET request to {uri}")
        r = requests.get(uri)
        logging.info(f"result: {r.status_code}")
        return r.content

    def get_data_as_string(self, uri):
        data = self._get_data_from_request(uri)
        return str(data)

    def get_data_as_dataframe(self, uri):
        data = self._get_data_from_request(uri)
        return pd.read_csv(StringIO(str(data)))

    def show_data(self):
        print(self)
