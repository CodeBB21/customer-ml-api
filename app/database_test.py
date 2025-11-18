from app.database import engine
from sqlalchemy import text

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Connexion OK →", list(result))
    except Exception as e:
        print("❌ Erreur de connexion :", e)


if __name__ == "__main__":
    test_connection()
