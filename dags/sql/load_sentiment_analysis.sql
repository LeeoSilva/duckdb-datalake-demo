COPY  -- noqa: PRS
(
    SELECT *
    FROM transformed_sentiment_analysis_data
)
TO ? (FORMAT PARQUET);
