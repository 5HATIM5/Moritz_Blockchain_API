# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

from models.products import Product


DATABASE_URL = "postgresql://postgres:admin@localhost:5432/BlockchainProductVerfirierDB"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

products_table = Product.__table__
