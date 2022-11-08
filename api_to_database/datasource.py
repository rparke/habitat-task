import requests
import pandas as pd
from io import StringIO
import logging
from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class DataSourceOne:
    """
    DataSource Object: for Database Consumer to Use
    """

    # Basic Placeholder function for validation, in practice MORE validation is neeeded.
    def _basic_validation(self, df: pd.DataFrame, uri: str):

        if all(
            item
            in [
                "_id",
                "Company",
                "Unit Name",
                "EFA Date",
                "Delivery Start",
                "Delivery End",
                "EFA",
                "Service",
                "Cleared Volume",
                "Clearing Price",
                "Technology Type",
                "Location",
                "Cancelled",
            ]
            for item in df.columns.values.tolist()
        ):
            logging.info(f"DataFrame read from uri: {uri} has valid column names")
        else:
            logging.error(f"Error")

    def get_data_as_df(self, uri: str) -> pd.DataFrame:
        df = pd.read_csv(
            uri,
        )
        self._basic_validation(df, uri)
        return df
