from fastapi import FastAPI
from .routers import health, ml, rag

app = FastAPI(
    title="Customer ML & RAG API",
    version="0.1.0",
    description="API FastAPI pour pipeline ML + LangChain/RAG déployée sur Render.",
)


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Customer ML & RAG API is running"}


# Register routers
app.include_router(health.router)
app.include_router(ml.router)
app.include_router(rag.router)

from .routers import customers, transactions

app.include_router(customers.router)
app.include_router(transactions.router)
