from dataclasses import dataclass
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Integer, Column, String, Boolean
from sqlalchemy import create_engine, select
from sqlalchemy.engine.base import Engine
from sqlalchemy.types import DateTime, Date


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


# engine = create_engine("sqlite://", echo=True)
# Base.metadata.create_all(engine)


# with Session(engine) as session:
#     example = AuctionResults(id=20, company_name="Richard's Company", unit_name="Power")
#     second_example = AuctionResults(
#         id=21, company_name="Richard's other Company", unit_name="Power"
#     )

#     session.add_all([example, second_example])
#     session.commit()

#     stmt = select(AuctionResults).where(AuctionResults.unit_name.in_(["Power"]))
#     for user in session.scalars(stmt):
#         print(user)
