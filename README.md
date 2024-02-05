# Moritz Blockchain Product Verifier (Backend)


This application seamlessly integrates blockchain technology with a product management system. The primary functionality revolves around maintaining a blockchain to ensure the integrity of product data. When new product information is submitted to the application, the blockchain processes the data and generates a unique hash. This hash, along with the product name, is then stored both in the blockchain and in the database.

This integrated system ensures a secure and tamper-resistant ledger for product-related information, combining the benefits of blockchain technology with efficient product management capabilities. Users can leverage the provided APIs to seamlessly interact with and manage both the blockchain and product data within the application.

This application features a dual-purpose journey management system catering to 
1. Administrators
2. Customers

The system seamlessly integrates blockchain technology with a product management system, offering distinct functionalities for each user role.

## Administrator Journey

For administrators, the system provides the capability to store product information securely within the blockchain and database. Upon adding a new product, an associated QR sticker is generated. This QR code contains crucial details about the product's authenticity, origin, and purity. Admins can affix these QR stickers to the respective products, thereby establishing a transparent and traceable record in the blockchain.

![alt text](https://github.com/5HATIM5/Moritz_Blockchain_API/blob/main/ReadMeImages/test.drawio.png)

## Blockchain Methods
![alt text](https://github.com/5HATIM5/Moritz_Blockchain_API/blob/main/ReadMeImages/blockchain.png)

## Products Methods
![alt text](https://github.com/5HATIM5/Moritz_Blockchain_API/blob/main/ReadMeImages/product.png)

## Customer Journey

On the customer journey side, the application introduces a product verification system. Customers utilize a dedicated app, the "Product Verifier," which allows them to scan the QR codes affixed to purchased products. Through this scanning process, customers can efficiently retrieve and verify detailed information about the product's origin, authenticity, and purity. This innovative approach enhances consumer trust by providing a direct means of verifying product details and ensuring the integrity of the supply chain.



## Blockchain Structure

**Description:**  This is how the blockchain structure looks like

**Response:**
```json
[
  {
    "index": 1,
    "timestamp": "2024-02-05 13:29:32.775990",
    "data": "genesis block",
    "proof": 1,
    "previous_hash": "0",
    "block_hash": "1442de2d7bffa42ff72a2ff0b5179e6d1b4157c3a4904a4d3dd35822ac11d25a"
  }
]
```
