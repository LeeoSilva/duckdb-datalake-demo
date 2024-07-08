CREATE TABLE IF NOT EXISTS price_search_raw_data AS 
SELECT *
FROM read_csv(?) -- noqa: PRS
