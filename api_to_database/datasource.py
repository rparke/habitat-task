import requests
import pandas as pd
from io import StringIO
import logging
from dataclasses import dataclass


@dataclass
class DataSource:
    """
    DataSource Object: for Database Consumer to Use
    """

    def _get_data_from_request(self, uri):
        logging.info(f"Sending GET request to {uri}")
        r = requests.get(uri)
        logging.info(f"result: {r.status_code}")
        return r.content

    def get_data_as_string(self, uri: str) -> str:
        data = self._get_data_from_request(uri)
        return str(data)

    def get_data_as_csv(self, uri: str) -> pd.DataFrame:
        data = str(self._get_data_from_request(uri))
        return pd.read_csv(StringIO(str(data)))

    def show_data(self):
        print(self)
