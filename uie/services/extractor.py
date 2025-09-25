"""Placeholder UIE extraction service."""

from typing import Any, Dict


def extract_information(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Simulate extracting structured information from an input payload."""
    print(f"[UIE] Extracting information from payload: {payload}")
    extraction = {"entities": [], "relations": []}
    print(f"[UIE] Extraction result: {extraction}")
    return extraction
