# docker build -t moin-backend -f docker/backend.dockerfile .

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

# uv Cache
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#caching
ENV UV_LINK_MODE=copy

# Install dependencies
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
WORKDIR /app
COPY ./pyproject.toml ./uv.lock ./

RUN uv sync --no-install-project --extra backend

COPY . .

# Sync the project
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "src/moin_moin/backend/api.py"]

