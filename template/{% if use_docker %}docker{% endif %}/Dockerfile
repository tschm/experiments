# syntax=docker/dockerfile:1.14
FROM python:3.13-slim

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.6.10 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Create non-root user early
RUN useradd -m app_user && \
    chown app_user:app_user /app

# Copy and install dependencies first for better caching
COPY --chown=app_user:app_user requirements.txt README.md notebooks /app/

# No dev dependencies,
RUN uv pip install --no-cache-dir -r requirements.txt && \
    rm -rf /uv /bin/uv

# Switch to non-root
USER app_user

# Expose the Flight server port
ENV PORT=8080
EXPOSE $PORT

# Set environment variables
ENV HOST=0.0.0.0

# Run the server
# CMD [".venv/bin/python", "{{ project_name }}/server.py"]
CMD marimo edit --no-token -p $PORT --host $HOST /app/notebooks
