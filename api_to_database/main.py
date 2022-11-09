import logging
from datasource import DataFrameClearner
from database_service import AuctionResultsDatabaseService
from sqlalchemy import create_engine
import pandas as pd

URI = "https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a"
database_url = (
    "sqlite://"  # we are simply using an in memory sqlite db for demonstration here
)
filter_companies = ["HABITAT ENERGY LIMITED"]


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info(f"Creating sqlalchemy engine for database at: {database_url}")
    engine = create_engine(database_url, echo=True)
    db_service = AuctionResultsDatabaseService()
    db_service.create_auction_results_table(engine=engine)
    db_service.add_results_to_database(
        engine=engine,
        df=DataFrameClearner().get_data_as_df(
            pd.read_csv(URI),
            filter_companies=filter_companies,
            rename_mapping={
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
            },
        ),
    )


if __name__ == "__main__":
    main()
