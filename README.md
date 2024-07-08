# Datalake GCP Demo 

## Cenary
You were hired as a Data Engineer to help launch a global craft marketplace,
where artists from around the world can sell their unique creations. This
marketplace aims to connect artisans with global customers, offering a variety
of products, from handmade jewelry to handmade furniture. Your mission is to
design and implement a robust data infrastructure that supports all business
operations, from product registration to sales and promotions analysis.

## Step 1: Data Modelling 
Create the database schema for this marketplace. It should include tables for
Customers who can be both buyers and sellers. A Product registration, which can
have varied attributes and be associated with different Stores, which are
managed by sellers and have their own profiles, Stock control to manage product
availability, and a sales record to track all transactions.

## Step 2: Data Ingestion
With the database schema defined, your next step is to design a Cloud Data Lake
architecture that integrates the marketplace database with external data sources.
This project should include two other data sources described below:
- Price Surveys: Integration of data obtained by a search robot. The data is
  deposited once a day, in CSV format, in an SFTP directory.

```csv
product_id,product_name,average_price,minimum_price,maximum_price,survey_date
prod-987654321,Bracelete Artesanal de Prata,150.0,140.0,160.0,2024-04-25
prod-123456789,Vaso de Cerâmica Pintado à Mão,120.0,100.0,140.0,2024-04-26
```

- Social Network Sentiment Analysis: The marketplace hired an API from a
  supplier that monitors social networks. This API generates an event every time
  it detects comments about the brand and its products.

```json 
{
"id": "evt-123456789",
"timestamp": "2024-04-25T14:30:00Z",
"text": "Adoro as joias deste marketplace! Sempre encontro peças únicas e de ótima
qualidade.",
"sentiment": {
"score": 0.95,
"label": "positivo"
},
"product": {
"id": "prod-987654321",
"name": "Bracelete Artesanal de Prata"
},
"user": {
"id": "usr-123456789",
"username": "artlover"
},
"source": "Twitter"
},
{
"id": "evt-987654321",
"timestamp": "2024-04-26T10:15:00Z",
"text": "Muito decepcionado com o serviço de entrega deste marketplace, demorou semanas e
o produto chegou danificado.",
"sentiment": {
"score": 0.2,
"label": "negativo"
},
"product": {
"id": "prod-123456789",
"name": "Vaso de Cerâmica Pintado à Mão"
},
"user": {
"id": "usr-987654321",
"username": "ceramicfan"
},
"source": "Facebook"
}
```

## Step 3: Data Transformation

Using the database schema and Data Lake architecture developed in the previous
steps, write a Python or SQL code (depending on your architecture choices) that
implements a data transformation of your choice. It should include data cleaning,
data combination (such as the marketplace database, price survey data, and social
network sentiment analysis, for example), and the creation of aggregations or
specific metrics that can support business decisions.
