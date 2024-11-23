from __future__ import annotations

from typing import Final

HOST: Final[str] = "http://127.0.0.1"
PORT: Final[int] = 8081
INSTITUTION_MAPPING: Final[dict[str, str]] = {
    "Police Department": "#48b5a5",
    "Fire Department": "#7b64ab",
    "Hospital": "#20be64",
    "Garbage Disposal": "#fb3c31",
    "Construction Department": "#0848da",
}
