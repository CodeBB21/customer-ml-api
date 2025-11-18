from fastapi import APIRouter
from ..rag.pipeline import RagQuery, RagAnswer, simple_rag_answer

router = APIRouter(prefix="/rag", tags=["rag"])


@router.post("/query", response_model=RagAnswer)
def rag_query(payload: RagQuery):
    """
    Endpoint RAG simple.
    Plus tard : on branchera sur un vrai vector store + embeddings + SQL.
    """
    return simple_rag_answer(payload)
