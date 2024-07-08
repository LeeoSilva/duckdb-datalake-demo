CREATE SEQUENCE IF NOT EXISTS seq_products_id START 1;

CREATE OR REPLACE TABLE products (
    id INT PRIMARY KEY DEFAULT NEXTVAL('seq_products_id'),
    prod_id VARCHAR(255) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
