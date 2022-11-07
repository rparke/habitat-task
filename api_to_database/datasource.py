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

    def _basic_validation(self, df: pd.DataFrame):
        print(df.columns.values.tolist())

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
            print("basic validation passed")
        else:
            print("error")

    def _rename_dataframe_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        rename_dict = {
            "_id": "id",
            "Company Name": "company_name",
            "Unit Name": "unit_name",
            "EFA Date": "efa_date",
            "Delivery Start": "delivery_start",
            "Delivery End": "delivery_end",
            "EFA": "efa",
            "Service": "service",
            "Cleared Volume": "cleared_volume",
            "Clearing Price": "clearing_price",
            "Technology Type": "technology_type",
            "Location": "location",
            "Cancelled": "cancelled",
        }
        df.rename(columns=rename_dict)
        return df

    def get_data_as_df(self, uri: str) -> pd.DataFrame:
        df = pd.read_csv(
            uri,
            dtype={
                "_id": int,
                "Company Name": str,
                "Unit Name": str,
                "EFA Date": date,
                "Delivery Start": datetime,
                "Delivery End": datetime,
                "EFA": int,
                "Service": str,
                "Cleared Volume": int,
                "Clearing Price": int,
                "Technology Type": str,
                "Location": str,
                "Cancelled": bool,
            },
        )
        self._basic_validation(df)
        return df
