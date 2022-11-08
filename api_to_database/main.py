import logging
from datasource import DataSourceAuctionResults
from database_writer import AuctionResults, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

URI = "https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a"
database_url = "sqlite://"


def main():
    logging.basicConfig(level=logging.INFO)
    ds = DataSourceAuctionResults(URI)
    df = ds.get_data_as_df()

    engine = create_engine(database_url, echo=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        test_entry = AuctionResults(id=df["_id"][0])


if __name__ == "__main__":
    main()
