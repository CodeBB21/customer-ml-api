from app.database import engine, Base
from app.models import *

print("📦 Création des tables dans PostgreSQL...")
Base.metadata.create_all(bind=engine)
print("✅ Tables créées avec succès !")
