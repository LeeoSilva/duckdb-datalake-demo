CREATE SEQUENCE IF NOT EXISTS seq_sentiment_status_id START 1;

CREATE TABLE IF NOT EXISTS sentiment_status ( 
    id INT PRIMARY KEY DEFAULT NEXTVAL('seq_sentiment_status_id'),
    status VARCHAR NOT NULL, 
    description VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sentiment_status (status, description)
VALUES 
('positive', 'A positive sentiment.'),
('negative', 'A negative sentiment.'),
('neutral', 'A neutral sentiment.');
