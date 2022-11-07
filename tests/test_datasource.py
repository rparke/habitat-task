import pandas as pd
from api_to_database.datasource import DataSource
import pytest


@pytest.fixture
def test_data():
    string_data = """
    
    """


def test_read():
    URI = "https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a"
    ds = DataSource()
    string_formatted_data = str(ds.get_data_as_string(URI))
    assert type(string_formatted_data) == str
