from __future__ import annotations

import os
from typing import Final

ENV = os.getenv("ENV", "local")
HOST = "localhost" if ENV in ("local", "dev") else "backend"
BACKEND_URL: Final[str] = f"http://{HOST}:8081"

INSTITUTION_COLOR_MAPPING: Final[dict[str, str]] = {
    "Police Department": "#48b5a5",
    "Fire Department": "#7b64ab",
    "Hospital": "#20be64",
    "Garbage Disposal": "#fb3c31",
    "Construction Department": "#0848da",
}
