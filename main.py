"""Entry point for the AI server FastAPI application."""

from fastapi import FastAPI

from rag import router as rag_router
from text2sql import router as text2sql_router
from uie import router as uie_router

app = FastAPI(title="AI Server", version="0.1.0")

app.include_router(uie_router)
app.include_router(rag_router)
app.include_router(text2sql_router)


@app.get("/", summary="Root endpoint")
async def root() -> dict[str, str]:
    """Simple root endpoint to confirm the service is running."""
    print("Root endpoint called")
    return {"message": "AI Server is running"}
