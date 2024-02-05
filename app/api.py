from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Depends
from fastapi import File, UploadFile
import fastapi as _fastapi

from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated
from pydantic import BaseModel
from sqlalchemy import insert, text
from sqlalchemy.orm import Session

from database import SessionLocal
import blockchain as _blockchain
from models.products import Product

blockchain = _blockchain.Blockchain()
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

origins = ["http://localhost:3000","" "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# DB CONNECTION CHECKER
@app.get("/dbConnection", tags=["Database Connection"])
async def check_db_connection(db: db_dependency):
    try:
        query = text("SELECT 1")

        db.execute(query)

        return {"Message": "Database connection is active"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error connecting to the database")


# BLOCKCHAIN
class ProductCreate(BaseModel):
    name: str
    production_location: str
    price: float
    production_date: str  # Assuming date is passed as a string in ISO format
    block_hash: str


# BLOCKCHAIN - Endpoint To Mine A Block
@app.post("/mine_block/", tags=["Blockchain Methods"])
# db: db_dependency
async def mine_block(data: str, ProductFormData: ProductCreate, db: db_dependency):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The Blockchain Is Invalid"
        )

    try:
        block = blockchain.mine_block(data=data)
        ProductFormData.block_hash = block["block_hash"]
        response = await store_product(db, ProductFormData)
        return {
            "message": "Block mined and product stored successfully",
            "block": block,
            "response": response,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# BLOCKCHAIN - Endpoint To Return A Blockchain
@app.get("/blockchain/", tags=["Blockchain Methods"])
async def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The Blockchain Is Invalid"
        )
    chain = blockchain.chain
    return chain


@app.post("/reset_blockchain", tags=["Blockchain Methods"])
async def reset_blockchain():
    blockchain.reset_chain()
    return {"message": "Blockchain reset successfully", "new_chain": blockchain.chain}

# BLOCKCHAIN - Endpoint To See If The Chain Is Valid
@app.get("/validate/", tags=["Blockchain Methods"])
async def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The Blockchain Is Invalid"
        )

    return blockchain.is_chain_valid()


# BLOCKCHAIN - Endpoint To Return The Last Block
@app.get("/blockchain/last/", tags=["Blockchain Methods"])
async def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The Blockchain Is Invalid"
        )

    return blockchain.get_previous_block()


# # CRUD FOR PRODUCTS - Endpoint To Store Products
@app.post("/store/product/", tags=["CRUD Product - Methods"])
async def store_product(db: db_dependency, product: ProductCreate):
    try:
        print(product)
        query = insert(Product).values(
            name=product.name,
            production_location=product.production_location,
            price=product.price,
            production_date=product.production_date,
            block_hash=product.block_hash,
        )
        result = db.execute(query)

        new_product_id = result.inserted_primary_key[0]

        db.commit()

        return {
            "Message": "Product created successfully",
            "id": new_product_id,
            "Product": jsonable_encoder(product),
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


# CRUD FOR PRODUCTS - Endpoint To Get All Products
@app.get("/products/", tags=["CRUD Product - Methods"])
async def get_all_products(db: db_dependency):
    try:
        products = db.query(Product).all()
        
        response_data = []

        if products:
            for product in products:
                product_data = {
                    "id": product.id,
                    "name": product.name,
                    "location": product.production_location,
                    "price": product.price,
                    "date": product.production_date,
                }
                response_data.append(product_data)

        return {"Message": "All Products Listed", "Response": response_data}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# CRUD FOR PRODUCTS - Endpoint To Get Product By ID
@app.get("/products/{product_id}", tags=["CRUD Product - Methods"])
async def get_products_by_id(db: db_dependency, product_id: int):
    try:
        product = db.query(Product).filter(Product.id == product_id).first()

        db.commit()

        db.refresh(product)

        return {"Message": "Product Listed", "Response": product}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# CRUD FOR PRODUCTS - Endpoint To Upload Products Image
@app.post("/store/product/image", tags=["CRUD Product - Methods"])
async def store_product_image(
    product_id: int,
    product_image: UploadFile = File(...),
):
    try:
        filename = f"{product_id}_{(product_image.filename)}"
        with open(f"uploads/{filename}", "wb") as f:
            f.write(product_image.file.read())

        return {"Message": "Image uploaded successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


class ProductUpdate(BaseModel):
    name: str
    production_location: str
    price: float
    production_date: str  # Assuming date is passed as a string in ISO format


# CRUD FOR PRODUCTS - Endpoint To Update Products
@app.put("/product/{product_id}", tags=["CRUD Product - Methods"])
async def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: Session = Depends(get_db),
):
    try:
        product = db.query(Product).filter(Product.id == product_id).first()

        if product:
            product.name = product_update.name
            product.production_location = product_update.production_location
            product.price = product_update.price
            product.production_date = product_update.production_date

            db.commit()
            db.refresh(product)

            return {
                "Message": "Product updated successfully",
                "Updated Product": jsonable_encoder(product),
            }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
