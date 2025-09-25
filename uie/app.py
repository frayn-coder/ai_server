"""UIE FastAPI router module."""

from fastapi import APIRouter

router = APIRouter(prefix="/uie", tags=["uie"])


@router.get("/status", summary="Check UIE module status")
async def get_status() -> dict[str, str]:
    """Return a simple status message for the UIE module."""
    print("UIE module status endpoint called")
    return {"message": "UIE module ready"}
