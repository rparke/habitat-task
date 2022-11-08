Assumptions:

1) The API data will be formatted "properly":
    - Column headings will be as expected
    - Pandas will deserialise the data types correctly ready to be added into the auction_results table. 
A placeholder method api_to_database.datasource.DataSourceAuctionResults._basic_validation has been added ready for logic that will validate both these assumptioins.

Running the Code:

Dependency management is by poetry




Main Next Steps:
    1) Development/Deployment containers (provides a reproducible production environment, and a reproducible development environment which all developers can use)
