import logging
from datasource import DataSourceAuctionResults
from database_service import AuctionResultsDatabaseService
from sqlalchemy import create_engine

URI = "https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a"
database_url = (
    "sqlite://"  # we are simply using an in memory sqlite db for demonstration here
)


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info(f"Creating sqlalchemy engine for database at: {database_url}")
    engine = create_engine(database_url, echo=True)
    db_service = AuctionResultsDatabaseService()
    db_service.create_auction_results_table(engine=engine)
    db_service.add_results_to_database(
        engine=engine, df=DataSourceAuctionResults(URI).get_data_as_df()
    )


if __name__ == "__main__":
    main()
