from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String, ForeignKey


Base = declarative_base()


class AuctionResults(Base):
    __tablename__ = "auction_results"

    id = Column(Integer, primary_key=True)


print(AuctionResults())
