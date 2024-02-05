# Moritz Blockchain Product Verifier (Backend)


This application seamlessly integrates blockchain technology with a product management system. The primary functionality revolves around maintaining a blockchain to ensure the integrity of product data. When new product information is submitted to the application, the blockchain processes the data and generates a unique hash. This hash, along with the product name, is then stored both in the blockchain and in the database.

This integrated system ensures a secure and tamper-resistant ledger for product-related information, combining the benefits of blockchain technology with efficient product management capabilities. Users can leverage the provided APIs to seamlessly interact with and manage both the blockchain and product data within the application.

This application features a dual-purpose journey management system catering to 
1. Administrators
2. Customers

The system seamlessly integrates blockchain technology with a product management system, offering distinct functionalities for each user role.

## 1. Administrator Journey

For administrators, the system provides the capability to store product information securely within the blockchain and database. Upon adding a new product, an associated QR sticker is generated. This QR code contains crucial details about the product's authenticity, origin, and purity. Admins can affix these QR stickers to the respective products, thereby establishing a transparent and traceable record in the blockchain.

![alt text](https://github.com/5HATIM5/Moritz_Blockchain_API/blob/main/ReadMeImages/test.drawio.png)

## 1.1 Blockchain Methods
![alt text](https://github.com/5HATIM5/Moritz_Blockchain_API/blob/main/ReadMeImages/blockchain.png)

## 1.2 Blockchain Structure

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
  },
 {
    "index": 2,
    "timestamp": "2024-02-05 13:30:32.775990",
    "data": "product_test_1",
    "proof": 452312,
    "previous_hash": "1442de2d7bffa42ff72a2ff0b5179e6d1b4157c3a4904a4d3dd35822ac11d25a",
    "block_hash": "123424nlk2lnk43knl2kn34knl2k43n234nkn2k3n4k2nl3k4k2n34n2482234knlkna"
  }
]
```

## 1.3 Products Methods
![alt text](https://github.com/5HATIM5/Moritz_Blockchain_API/blob/main/ReadMeImages/product.png)

## 2. Customer Journey

On the customer journey side, the application introduces a product verification system. Customers utilize a dedicated app, the "Product Verifier," which allows them to scan the QR codes affixed to purchased products. Through this scanning process, customers can efficiently retrieve and verify detailed information about the product's origin, authenticity, and purity. This innovative approach enhances consumer trust by providing a direct means of verifying product details and ensuring the integrity of the supply chain.

![alt text](https://github.com/5HATIM5/Moritz_Blockchain_API/blob/main/ReadMeImages/customer.drawio.png)

