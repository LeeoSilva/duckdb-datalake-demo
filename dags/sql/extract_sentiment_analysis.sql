CREATE TABLE IF NOT EXISTS sentiment_analysis_raw_data AS
SELECT *
FROM read_json(?) -- noqa: PRS
