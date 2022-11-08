from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String


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
