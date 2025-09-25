"""Route definitions for the RAG module."""

from fastapi import APIRouter

from ..services.pipeline import run_retrieval_pipeline

router = APIRouter(prefix="/rag", tags=["rag"])


@router.post("/search", summary="Search documents using RAG")
def search_documents(query: str) -> dict:
    """Run the retrieval pipeline for a given query."""
    result = run_retrieval_pipeline(query=query)
    return {"query": query, "result": result}
