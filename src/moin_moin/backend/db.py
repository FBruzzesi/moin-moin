import sqlite3

import numpy as np

DB = "images.db"
TABLE = "images"


def create_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE} (
        image BLOB,
        embedding BLOB,
        latitude REAL,
        longitude REAL,
        notes TEXT,
        tags TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_img(
    *,
    image: np.ndarray,
    embedding: np.ndarray,
    latitude: float,
    longitude: float,
    notes: str,
    tags: str,
):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        f"""
    INSERT INTO {TABLE} (image, embedding, latitude, longitude, notes, tags)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
        (
            # Make sure the type is float64 for later loading
            image.astype(np.float64).tobytes(),
            embedding.astype(np.float64).tobytes(),
            latitude,
            longitude,
            notes,
            tags,
        ),
    )
    conn.commit()
    conn.close()


# if __name__ == "__main__":
#     create_db()
