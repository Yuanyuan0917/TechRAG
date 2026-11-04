"""FastAPI application for the local TechRAG demo."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from .routes_query import TechRAGService, router


def create_app(query_service: TechRAGService | None = None) -> FastAPI:
    """Create the API with one application-scoped TechRAG service."""
    service = query_service or TechRAGService()

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        yield
        await service.close()

    application = FastAPI(
        title="TechRAG API",
        version="0.1.0",
        lifespan=lifespan,
    )
    application.state.query_service = service
    application.include_router(router)
    return application


app = create_app()
