"""Route definitions for the UIE module."""

from fastapi import APIRouter

from ..services.extractor import extract_information

router = APIRouter(prefix="/uie", tags=["uie"])


@router.post("/extract", summary="Extract structured information")
def extract(payload: dict) -> dict:
    """Extract structured information from an input payload."""
    extraction = extract_information(payload=payload)
    return {"payload": payload, "extraction": extraction}
