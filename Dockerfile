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

CMD ["uv", "run", "backend/app.py"]
