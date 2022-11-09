import pytest
import pandas as pd
from api_to_database.datasource import DataFrameClearner


@pytest.fixture
def df():
    data = {
        "COLUMN_A": [1, 2, 3, 4, 5],
        "COLUMN_B": [6, 7, 8, 9, 10],
        "Company": [
            "HABITAT ENERGY LIMITED",
            "HABITAT ENERGY LIMITED",
            "HABITAT ENERGY LIMITED",
            "SOME OTHER COMPANY",
            "ANOTHER COMPANY",
        ],
    }
    return pd.DataFrame.from_dict(data)


@pytest.fixture
def rename_mapping():
    return {"COLUMN_A": "a", "COLUMN_B": "b", "Company": "company"}


@pytest.fixture
def filter_companies():
    return ["HABITAT ENERGY LIMITED"]


def test_renaming(df, rename_mapping, filter_companies):
    cleaner = DataFrameClearner()
    df = cleaner.get_data_as_df(
        df=df,
        rename_mapping=rename_mapping,
        filter_companies=filter_companies,
    )
    assert "a" in df.columns
    assert "b" in df.columns
    assert "company" in df.columns
    assert "COLUMN_A" not in df.columns
    assert "COLUMN_B" not in df.columns
    assert "Company" not in df.columns


def test_filtering(df, rename_mapping, filter_companies):
    cleaner = DataFrameClearner()
    df = cleaner.get_data_as_df(
        df=df,
        rename_mapping=rename_mapping,
        filter_companies=filter_companies,
    )
    assert "HABITAT ENERGY LIMITED" in list(df["company"])
    assert "SOME OTHER COMPANY" not in list(df["company"])
    assert "ANOTHER COMPANY" not in list(df["company"])
