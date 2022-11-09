from sqlalchemy import create_engine, inspect, select
from sqlalchemy.orm import Session
from api_to_database.database_service import (
    AuctionResults,
    AuctionResultsDatabaseService,
)
import pytest
from api_to_database.datasource import DataFrameClearner
import pandas as pd

# Refactor into a Mock
@pytest.fixture
def engine():
    return create_engine("sqlite://")


# Refactor to not depend on API or DataFrameCleaner.get_data_as_df method
@pytest.fixture
def cleaned_df():
    URI = "https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a"
    filter_companies = ["HABITAT ENERGY LIMITED"]
    rename_mapping = {
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
    }

    return DataFrameClearner().get_data_as_df(
        df=pd.read_csv(URI),
        filter_companies=filter_companies,
        rename_mapping=rename_mapping,
    )


def test_create_auction_results_table(engine):
    db_service = AuctionResultsDatabaseService()
    db_service.create_auction_results_table(engine)
    insp = inspect(engine)
    assert "auction_results" in insp.get_table_names()


def test_add_results_to_database(engine, cleaned_df):
    db_service = AuctionResultsDatabaseService()
    db_service.create_auction_results_table(engine)
    db_service.add_results_to_database(engine=engine, df=cleaned_df)
    stmt = select(AuctionResults).where(
        AuctionResults.company.in_(["HABITAT ENERGY LIMITED"])
    )
    with Session(engine) as session:
        assert len(list(session.scalars(stmt))) > 0
