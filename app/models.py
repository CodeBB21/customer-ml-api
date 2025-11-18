from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relation 1 → N avec transactions
    transactions = relationship("Transaction", back_populates="customer")


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    amount = Column(Float)
    category = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="transactions")


class ModelMetadata(Base):
    """
    Stockage des modèles ML déployés (versioning)
    """
    __tablename__ = "ml_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    version = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    description = Column(Text)
    artifact_path = Column(String)  # Chemin vers un fichier modèle dans ton repo ou cloud


class Embedding(Base):
    """
    Table pour ton futur système RAG : vecteurs embeddings en base
    """
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    vector = Column(Text)  # on stocke le vecteur converti en string (JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
