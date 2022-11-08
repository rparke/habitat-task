import pandas as pd
import logging
from dataclasses import dataclass


@dataclass
class DataSourceAuctionResults:
    """
    DataSource Object: for Database Consumer to Use
    """

    uri: str

    # Basic Placeholder function for validation, in practice MORE validation is neeeded.
    def _basic_validation(self):

        logging.info("Validation will always pass")

    def get_data_as_df(self) -> pd.DataFrame:
        self._df = pd.read_csv(
            self.uri,
        )
        self._basic_validation()
        return self._df
