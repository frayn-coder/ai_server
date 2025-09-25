"""RAG FastAPI router module."""

from fastapi import APIRouter

router = APIRouter(prefix="/rag", tags=["rag"])


@router.get("/status", summary="Check RAG module status")
async def get_status() -> dict[str, str]:
    """Return a simple status message for the RAG module."""
    print("RAG module status endpoint called")
    return {"message": "RAG module ready"}
