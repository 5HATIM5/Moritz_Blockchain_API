from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models.products import Product


BETA_DATABASE_URL = "postgresql://mweehgan:uXCZEAZkQbjg8Msrh23JzGgiUc5HCCaP@snuffleupagus.db.elephantsql.com/mweehgan"
LOCAL_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/BlockchainProductVerfirierDB"

engine = create_engine(LOCAL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

products_table = Product.__table__
