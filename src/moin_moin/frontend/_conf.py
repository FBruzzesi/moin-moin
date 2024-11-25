from __future__ import annotations

import os
from typing import Final

ENV = os.getenv("ENV", "local")
HOST = "localhost" if ENV in ("local", "dev") else "backend"
BACKEND_URL: Final[str] = f"http://{HOST}:8081"

INSTITUTION_COLOR_MAPPING: Final[dict[str, str]] = {
    "Infrastructure": "#50734e",
    "Public Safety": "#756d4d",
    "Waste Management and Cleanliness": "#e6b710",
    "Public Amenities and Facilities": "#7921c2",
    "Street Signage and Markings": "#db0ba7",
}
