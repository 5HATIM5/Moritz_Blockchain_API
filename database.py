from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models.products import Product


DATABASE_URL = "postgresql://mweehgan:uXCZEAZkQbjg8Msrh23JzGgiUc5HCCaP@snuffleupagus.db.elephantsql.com/mweehgan"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

products_table = Product.__table__
