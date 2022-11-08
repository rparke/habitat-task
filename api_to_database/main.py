import logging
from datasource import DataSourceAuctionResults
from database_writer import AuctionResults, Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

URI = "https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a"
database_url = "sqlite://"


def add_auction_results_to_database(engine, listToWrite):
    with Session(engine) as session:
        session.add_all([AuctionResults(**item) for item in listToWrite])
        session.commit()


def read_auction_results_from_database(
    engine, company_names=["HABITAT ENERGY LIMITED"]
):

    with Session(engine) as session:

        stmt = select(AuctionResults).where(AuctionResults.company.in_(company_names))

        for results in session.scalars(stmt):
            print(results)


def main():
    logging.basicConfig(level=logging.INFO)
    ds = DataSourceAuctionResults(URI)
    df = ds.get_data_as_df()

    engine = create_engine(database_url, echo=True)
    Base.metadata.create_all(engine)
    listToWrite = df.to_dict(orient="records")

    add_auction_results_to_database(engine, listToWrite)

    read_auction_results_from_database(engine)


if __name__ == "__main__":
    main()
