WITH transformed_sentiment_analysis_data AS (
    SELECT 
        product_id,
        product_name,
        average_price,
        minimum_price,
        maximum_price,
        survey_date
    FROM raw_data
)

INSERT INTO price_search_fact(
    id, 
    product_id,
    average_price,
    minimum_price,
    maximum_price,
    survey_date
)
SELECT 
    (nextval('seq_price_search_fact_id')),
    transformed_sentiment_analysis_data.product_id,
    transformed_sentiment_analysis_data.average_price,
    transformed_sentiment_analysis_data.minimum_price,
    transformed_sentiment_analysis_data.maximum_price,
    transformed_sentiment_analysis_data.survey_date
FROM transformed_sentiment_analysis_data 
