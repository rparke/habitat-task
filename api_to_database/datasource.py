import pandas as pd
import logging
import datetime


class DataFrameClearner:
    """
    DataSource Object: for Database Consumer to Use
    """

    def __init__(self):
        pass

    # Basic Placeholder function for validation, in practice MORE validation is neeeded.
    def _basic_validation(self):
        logging.info("Validating...")
        logging.info("Validation passed because validation will always pass")

    def _rename_columns(self, rename_mapping):
        self._df = self._df.rename(columns=rename_mapping)

    def _filter_out_companies(self, filter_companies):
        self._df = self._df[self._df["company"].isin(filter_companies)]

    def get_data_as_df(
        self,
        df,
        filter_companies,
        rename_mapping,
    ):
        self._df = df
        self._basic_validation()
        self._rename_columns(rename_mapping)
        self._filter_out_companies(filter_companies)
        return self._df
