CREATE SEQUENCE IF NOT EXISTS seq_sentiment_analysis_fact_id START 1;

CREATE TABLE IF NOT EXISTS sentiment_analysis_fact (
    id INT PRIMARY KEY DEFAULT NEXTVAL('seq_sentiment_analysis_fact_id'),
    comment VARCHAR NOT NULL,
    sentiment_score DECIMAL(10, 2) NOT NULL,
    sentiment_status_id INT NOT NULL,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    source_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL
);
