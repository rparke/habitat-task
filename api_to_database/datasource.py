import pandas as pd
import logging


class DataSourceAuctionResults:
    """
    DataSource Object: for Database Consumer to Use
    """

    def __init__(self, uri):
        self.uri = uri
        self.filter_companies = ["HABITAT ENERGY LIMITED"]

    # Basic Placeholder function for validation, in practice MORE validation is neeeded.
    def _basic_validation(self):

        logging.info("Validation will always pass")

    def _rename_columns(self):
        self._df = self._df.rename(
            columns={
                "_id": "id",
                "Company": "company",
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
        )

    def _filter_out_companies(self):
        self._df = self._df[self._df["company"].isin(self.filter_companies)]

    def get_data_as_df(self) -> pd.DataFrame:
        self._df = pd.read_csv(
            self.uri,
        )
        self._basic_validation()
        self._rename_columns()
        self._filter_out_companies()
        return self._df
