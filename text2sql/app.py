"""Text2SQL FastAPI router module."""

from fastapi import APIRouter

router = APIRouter(prefix="/text2sql", tags=["text2sql"])


@router.get("/status", summary="Check Text2SQL module status")
async def get_status() -> dict[str, str]:
    """Return a simple status message for the Text2SQL module."""
    print("Text2SQL module status endpoint called")
    return {"message": "Text2SQL module ready"}
