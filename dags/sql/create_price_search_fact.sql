CREATE TABLE IF NOT EXISTS price_search_fact ( 
    id INT PRIMARY KEY,
    product_id VARCHAR NOT NULL,
    average_price DECIMAL(10, 2) NOT NULL,
    minimum_price DECIMAL(10, 2) NOT NULL,
    maximum_price DECIMAL(10, 2) NOT NULL,
    survey_date DATETIME NOT NULL
);

CREATE SEQUENCE IF NOT EXISTS seq_price_search_fact_id START 1;
