from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER_BD = "jcanabal"
PSW_BD = "psw"
HOST = "localhost"
PORT = "5432"
DB = "aerolineadb"

# engine = create_engine(f"postgresql://{USER_BD}:{PSW_BD}@{HOST}:{PORT}/{DB}")
engine = create_engine("postgresql://jcanabal:psw@localhost:5432/jcanabal")

Base = declarative_base()

conect = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
