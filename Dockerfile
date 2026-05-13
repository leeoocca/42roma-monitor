FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies with uv
RUN uv sync --frozen --no-dev

# Copy project
COPY . .

# Expose the internal app port
EXPOSE 8000

# Run with gunicorn in production
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "backend.app:app"]
