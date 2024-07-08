WITH transformed_price_search_data AS (
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
    transformed_price_search_data.product_id,
    transformed_price_search_data.average_price,
    transformed_price_search_data.minimum_price,
    transformed_price_search_data.maximum_price,
    transformed_price_search_data.survey_date
FROM transformed_price_search_data
