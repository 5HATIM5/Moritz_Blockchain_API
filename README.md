# Moritz Blockchain API

This FastAPI-based API manages a blockchain and provides endpoints for adding products to the database. The blockchain stores product data along with a generated hash for data integrity. Additionally, the API includes endpoints for mining new blocks, retrieving the entire blockchain, resetting the blockchain, validating its integrity, and fetching the previous block.


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
