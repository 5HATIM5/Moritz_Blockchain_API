# Moritz Blockchain Product Verifier


This FastAPI-based application seamlessly integrates blockchain technology with a product management system. The primary functionality revolves around maintaining a blockchain to ensure the integrity of product data. When new product information is submitted to the application, the blockchain processes the data and generates a unique hash. This hash, along with the product name, is then stored both in the blockchain and in the database.

The application offers a comprehensive set of APIs to interact with and manipulate both the blockchain and product data. Users can mine new blocks, retrieve the entire blockchain, reset it to the genesis block, validate its integrity, and fetch details about the previous block. Additionally, the application facilitates product-related operations, such as storing new products in the database, retrieving product information, storing product images, and updating existing product data.

This integrated system ensures a secure and tamper-resistant ledger for product-related information, combining the benefits of blockchain technology with efficient product management capabilities. Users can leverage the provided APIs to seamlessly interact with and manage both the blockchain and product data within the application.


## Endpoints

### 1. Check Database Connection

**Endpoint:** `GET /dbConnection`

**Description:**  Checks the connection to the database..

**Response:**
```json
{
  "Message": "Database connection is active"
}
```
