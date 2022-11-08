import logging
from datasource import DataSourceOne

URI = "https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a"


def main():
    logging.basicConfig(level=logging.INFO)
    ds = DataSourceOne(URI)
    df = ds.get_data_as_df()
    print(df)


if __name__ == "__main__":
    main()
