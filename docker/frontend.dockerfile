# docker build -t moin-frontend -f docker/frontend.dockerfile .

FROM python:3.12-slim-bookworm

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists /var/cache

# Download, install and remove the latest uv installer
RUN curl -LsSf -o /uv-installer.sh https://astral.sh/uv/0.5.1/install.sh && \
    sh /uv-installer.sh && \
    rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Env variables
ENV UV_COMPILE_BYTECODE=1
ENV UV_SYSTEM_PYTHON=1

# uv Cache
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#caching
ENV UV_LINK_MODE=copy

# Install dependencies
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
WORKDIR /app
COPY ./pyproject.toml ./uv.lock ./

RUN uv sync --no-install-project --extra frontend

COPY . .

# Sync the project
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
RUN uv sync

EXPOSE 8501

ENTRYPOINT ["uv", "run", "streamlit", "run", "src/moin_moin/frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

