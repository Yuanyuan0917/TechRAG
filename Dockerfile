FROM python:3.11.14-slim-bookworm AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app
RUN useradd --create-home --uid 10001 techrag

FROM base AS api

COPY docker/requirements-api.txt /tmp/requirements-api.txt
# CPU wheels avoid installing a CUDA runtime into this local development image.
RUN python -m pip install --no-cache-dir torch==2.8.0 --index-url https://download.pytorch.org/whl/cpu \
    && python -m pip install --no-cache-dir -r /tmp/requirements-api.txt

COPY app/ app/
COPY scripts/ingest.py scripts/ingest.py
RUN mkdir -p data/raw /home/techrag/.cache/huggingface \
    && chown -R techrag:techrag /home/techrag/.cache
ENV HF_HOME=/home/techrag/.cache/huggingface
USER techrag
EXPOSE 8000
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM base AS frontend

COPY docker/requirements-frontend.txt /tmp/requirements-frontend.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements-frontend.txt
COPY frontend/ frontend/
USER techrag
EXPOSE 8501
CMD ["streamlit", "run", "frontend/streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true", "--browser.gatherUsageStats=false"]
