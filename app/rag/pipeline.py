from pydantic import BaseModel
from ..config import settings

try:
    from langchain_core.prompts import PromptTemplate
    from langchain_openai import ChatOpenAI  # nécessite `openai` + `langchain-openai`
    LANGCHAIN_AVAILABLE = True
except Exception:
    LANGCHAIN_AVAILABLE = False


class RagQuery(BaseModel):
    question: str


class RagAnswer(BaseModel):
    answer: str
    info: str | None = None


def simple_rag_answer(query: RagQuery) -> RagAnswer:
    """
    Placeholder RAG : utilise ChatOpenAI si dispo, sinon renvoie un message explicite.
    Plus tard : remplacer par un vrai pipeline RAG (embeddings + vector store SQL, etc.).
    """
    if not LANGCHAIN_AVAILABLE:
        return RagAnswer(
            answer="RAG non disponible : dépendances LangChain manquantes.",
            info="Installez 'langchain-core' + 'langchain-openai' pour activer ce pipeline.",
        )

    if not settings.OPENAI_API_KEY:
        return RagAnswer(
            answer="RAG non configuré : aucune clé OPENAI_API_KEY définie.",
            info="Définissez la variable d'environnement OPENAI_API_KEY sur Render.",
        )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, api_key=settings.OPENAI_API_KEY)

    prompt = PromptTemplate(
        input_variables=["question"],
        template=(
            "Tu es un assistant pour un système RAG de démo.\n"
            "Réponds brièvement et clairement à la question suivante : {question}"
        ),
    )

    chain = prompt | llm

    result = chain.invoke({"question": query.question})
    return RagAnswer(answer=result.content, info="Réponse générée par ChatOpenAI.")
