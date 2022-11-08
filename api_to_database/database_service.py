from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Integer, Column, String, exc
import logging


Base = declarative_base()


class AuctionResults(Base):
    __tablename__ = "auction_results"

    # Simplified, data and datetime objects just represented as strings
    id = Column(Integer, primary_key=True)
    company = Column(String)
    unit_name = Column(String)
    efa_date = Column(String)
    delivery_start = Column(String)
    delivery_end = Column(String)
    efa = Column(Integer)
    service = Column(String)
    cleared_volume = Column(Integer)
    clearing_price = Column(Integer)
    technology_type = Column(String)
    location = Column(String)
    cancelled = Column(String)

    def __repr__(self):
        return f"ID: {self.id}, Company Name: {self.company}"


class AuctionResultsDatabaseService:
    def __init__(self):
        pass

    def add_results_to_database(self, engine, df):
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

    def create_auction_results_table(self, engine):
        logging.info(f"Creating Table: {AuctionResults.__tablename__}")
        Base.metadata.create_all(engine)
