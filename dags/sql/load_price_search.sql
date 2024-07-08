COPY  -- noqa: PRS
(
    SELECT *
    FROM transformed_price_search_data 
)
TO ? (FORMAT PARQUET);
