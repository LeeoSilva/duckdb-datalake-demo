CREATE SEQUENCE IF NOT EXISTS seq_stock_control_id START 1;

CREATE OR REPLACE TABLE stock_control (
    id INT PRIMARY KEY DEFAULT NEXTVAL('seq_stock_control_id'),
    product_id INT NOT NULL,
    store_id INT NOT NULL,
    quantity INT NOT NULL,
    last_updated TIMESTAMP NOT NULL
);
