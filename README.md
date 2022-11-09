Assumptions:

1) The API data will be formatted "properly":
    - Column headings will be as expected
    - Pandas will deserialise the data types correctly ready to be added into the auction_results table. 
A placeholder method api_to_database.datasource.DataSourceAuctionResults._basic_validation has been added ready for logic that will validate both these assumptioins.

2) The IDs for each bid are unique and bidding results do not change once they are published. We can therefore use these IDs as Primary Keys

3) All data are either strings or ints (in practice the datasource.DataFramCleaner class should be written so that Date/DateTime data is of the correct type, with the db Table written so that data of that type can be inserted and correctly queried afterwards)

4) We only care about Habitat's Auction results. We currently use the DataFrameCleaner to filter out all other companies apart from habitat.

Running the Code:
    1) Dependency management is taken care of by Poetry, instructions for installing poetry and the environment for running the code are found here: https://python-poetry.org/

    2) Once poetry has installed the environment, initialise a shell with poetry shell. This can then be used for running api_to_database main.py and the tests

    3) To run the example where a database is initialised and written to with "cleaned" data from the API just run python api_to_database.main.py

    4) To run tests, run pytest from the root of the directory


Main Next Steps:
(This is not an exhaustive list, but what I have identified as the main issues with the code/tests at present. In most cases these next steps have either been commented where relavent or inserted as placeholder methods)
    1) Development/Deployment containers (provides a reproducible production environment, and a reproducible development environment which all developers can use)

    2) Dealing with Duplicate Entries. At present any duplicate entry (specifically duplicate primary key) will raise an exception and the insert will fail. In practice we should either update an entry OR create a composite key out of the ID and the timestamp of when the API was accessed (depending upon whether we expect data to change etc)

    3) Implement Validation of the Dataframe. At present no validation of the data happens, and so there are no guarantees that all the expected columns exist, that the series types are as expected etc. This could therefore easily break (without useful warning) if the APIs schema for its data changes etc.

    4) Rewrite the test_database_service fixtures so that they do not depend on a real database (even though it is in memory) and so that they do not depend on an API (bad because the API could cease to exist, its format and contents could change, etc), and as currently written it requires the DataFrameCleaner class to work correctly too (the unit test should only test a single unit)
    
    5) Insert UTC timestamps into the db table, so that data scientists etc. are aware of WHEN the data was first made available.
