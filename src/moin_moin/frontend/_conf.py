from __future__ import annotations

import os
from typing import Final

ENV = os.getenv("ENV", "local")
HOST = "localhost" if ENV in ("local", "dev") else "backend"
BACKEND_URL: Final[str] = f"http://{HOST}:8081"

INSTITUTION_MAPPING: Final[dict[str, str]] = {
    "Infrastructure": "#48b5a5",
    "Public Safety": "#7b64ab",
    "Waste Management and Cleanliness": "#20be64",
    "Public Amenities and Facilities": "#fb3c31",
    "Street Signage and Markings": "#f7bb97",
}
