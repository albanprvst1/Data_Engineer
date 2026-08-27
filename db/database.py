from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Float, Integer, String

# 1. Définir l'URL de connexion SQLite
# Le préfixe "sqlite:///" indique un fichier SQLite local nommé "bourse.db"
DATABASE_URL = "sqlite:///bourse.db"

# 2. Créer le moteur de connexion (Engine)
engine = create_engine(DATABASE_URL, echo=True)

# 3. Créer une classe de base pour nos modèles de tables
Base = declarative_base()

# 4. Créer un fabrique de sessions pour interagir avec la base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class ETFData(Base):
    __tablename__ = "etf_prices"

    ticker = Column(String(),primary_key=True)
    date = Column(String())
    open_price = Column(Float())
    close_price = Column(Float())
    high_price = Column(Float())
    low_price = Column(Float())
    volume = Column(Integer())

def init_db():
    Base.metadata.create_all(bind=engine)