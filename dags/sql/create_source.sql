CREATE SEQUENCE IF NOT EXISTS seq_source_id START 1;

CREATE TABLE IF NOT EXISTS sources (
    id INT PRIMARY KEY DEFAULT NEXTVAL('seq_source_id'),
    source_name VARCHAR NOT NULL,
    url VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sources (source_name, url)
VALUES 
('Twitter', 'https://twitter.com/'),
('Facebook', 'https://www.facebook.com/'),
('Instagram', 'https://www.instagram.com/'),
('Reddit', 'https://www.reddit.com/');
