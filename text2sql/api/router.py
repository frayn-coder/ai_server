"""Route definitions for the Text2SQL module."""

from fastapi import APIRouter

from ..services.generator import generate_sql_query

router = APIRouter(prefix="/text2sql", tags=["text2sql"])


@router.post("/generate", summary="Generate SQL from natural language")
def generate_sql(prompt: str) -> dict:
    """Convert a natural language prompt into a SQL query."""
    sql_statement = generate_sql_query(prompt=prompt)
    return {"prompt": prompt, "sql": sql_statement}
