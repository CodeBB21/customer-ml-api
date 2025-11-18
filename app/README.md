# Customer ML & RAG API

API FastAPI déployable sur Render qui expose :

- `/health` : health check
- `/ml/predict` : mini modèle ML de démo
- `/rag/query` : endpoint RAG basé sur LangChain (placeholder pour l'instant)

## Démarrage local

```bash
conda create -n customer_api python=3.10 -y
conda activate customer_api

pip install -r requirements.txt

uvicorn app.main:app --reload
