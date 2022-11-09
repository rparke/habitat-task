import pandas as pd
import logging


class DataFrameClearner:
    """
    Generic DataFrame Cleaner. Performs validation of the incomming dataframe,
    renames columns so they adhere to the tables schema, and filters out companies not of interest
    """

    def __init__(self):
        pass

    def _basic_validation(self):
        """Placeholder Function for Validation"""
        logging.info("Validating...")
        logging.info("Validation passed because validation will always pass")

    def _rename_columns(self, rename_mapping):
        """Generic Function for Renaming Columns to Fit to a Schema"""
        self._df = self._df.rename(columns=rename_mapping)

    def _filter_out_companies(self, filter_companies):
        """
        Problem specific function to filter out specific comapnies.
        Going forward this should probably be rewritten as more generic
        by passing a dict of key value pairs containing the key to filter, and the values to filter out
        """
        self._df = self._df[self._df["Company"].isin(filter_companies)]

    def _clean_up_data(self):
        logging.info(
            "clean up dateframe data: Not Implemented Yet! Will ensure that series adhere to the correct types"
        )

    def get_data_as_df(
        self,
        df,
        filter_companies,
        rename_mapping,
    ):
        self._df = df
        self._basic_validation()
        self._filter_out_companies(filter_companies)
        self._rename_columns(rename_mapping)
        self._clean_up_data()
        return self._df
