# Blockchain API

This is a simple FastAPI-based API for managing a basic blockchain. The API includes endpoints for mining new blocks, retrieving the entire blockchain, resetting the blockchain, validating its integrity, and fetching the previous block.

## Endpoints

### 1. Mine Block

**Endpoint:** `POST /mine_block/`

**Description:** Mines a new block and adds it to the blockchain.

**Request:**
```json
{
  "data": "Your data for the new block"
}
