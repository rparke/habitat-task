import logging
from datasource import DataSourceAuctionResults
from database_writer import AuctionResults, Base
from sqlalchemy import create_engine, select, exc
from sqlalchemy.orm import Session

URI = "https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a"
database_url = (
    "sqlite://"  # we are simply using an in memory sqlite db for demonstration here
)


def add_auction_results_to_database(engine, df):

    with Session(engine) as session:
        try:
            session.add_all(
                [AuctionResults(**item) for item in df.to_dict(orient="records")]
            )
            session.commit()
        except exc.SQLAlchemyError as e:
            logging.error(
                f"Attempting to insert new data into query resulted in exception {e}"
            )


def read_auction_results_from_database(
    engine, company_names=["HABITAT ENERGY LIMITED"]
):

    with Session(engine) as session:

        stmt = select(AuctionResults).where(AuctionResults.company.in_(company_names))

        for results in session.scalars(stmt):
            print(results)


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info(f"GET DataFrame from {URI}")
    df = DataSourceAuctionResults(URI).get_data_as_df()

    logging.info(f"Creating sqlalchemy engine for database at: {database_url}")
    engine = create_engine(database_url)
    logging.info(f"Creating Table: {AuctionResults.__tablename__}")
    Base.metadata.create_all(engine)
    logging.info("First Attempt")
    add_auction_results_to_database(engine, df)
    logging.info("Second Attempt")
    add_auction_results_to_database(engine, df)
    logging.info("Third Attempt")
    add_auction_results_to_database(engine, df)

    # read_auction_results_from_database(engine)


if __name__ == "__main__":
    main()
