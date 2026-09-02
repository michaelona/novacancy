
"""
lot_history_api.py

This is a sanitized example of NoVacancy's Flask backend endpoints.

Demonstrates:
- API-key authentication
- Input validation
- Parameterized PostgreSQL queries
- Database connection management
- JSON serialization

"""

import os
from contextlib import contextmanager

import psycopg2
import psycopg2.extras
from flask import Flask, jsonify, request

app = Flask(__name__)

# Database credentials are supplied through environment variables
# rather than being hardcoded into source code.
DB_CONFIG = {
    "dbname": os.environ["DB_NAME"],
    "host": os.environ["DB_HOST"],
    "port": os.environ.get("DB_PORT", 5432),
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASS"],
}

API_KEY = os.environ.get("API_KEY", "")
MAX_LIMIT = 2000

# Approved lot_codes for validating requests.
VALID_LOT_CODES = {
    "CD FS",
    "CD VS",
    "CRI",
    "ED1",
    "ED2/3",
    "NORTH",
    "SOUTH",
    "UDL",
    "UDU",
    "WEST",
}


def check_api_key():
    """Require API-key authentication when configured."""
    if not API_KEY:  # Local development only.
        return None

    if request.headers.get("X-API-Key") != API_KEY:
        return jsonify({"error": "unauthorized"}), 401

    return None


@contextmanager
def db_cursor():
    """
    Opens a PostgreSQL connection and yield a dictionary-style cursor.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor
    )

    try:
        yield cur
    finally:
        cur.close()
        conn.close()


@app.route("/lots/<path:lot_code>/history")
def get_lot_history(lot_code):
    # 1. Authenticate first
    error = check_api_key()
    if error:
        return error

    # 2. Validate that the requested lot is known.
    if lot_code not in VALID_LOT_CODES:
        return jsonify({
            "error": "unknown lot_code",
            "lot_code": lot_code,
        }), 404

    # 3. Read any optional query parameters and set the default row count.
    start = request.args.get("start")
    end = request.args.get("end")

    limit = min(
        request.args.get("limit", default=100, type=int),
        MAX_LIMIT,
    )

    # 4. Query PostgreSQL using parameters.
    with db_cursor() as cur:
        if start and end:
            cur.execute(
                """
                SELECT timestamp, percent_available
                FROM occupancy_readings
                WHERE lot_code = %s
                  AND timestamp >= %s
                  AND timestamp <= %s
                ORDER BY timestamp ASC
                LIMIT %s
                """,
                (lot_code, start, end, limit),
            )
        else:
            cur.execute(
                """
                SELECT timestamp, percent_available
                FROM occupancy_readings
                WHERE lot_code = %s
                ORDER BY timestamp DESC
                LIMIT %s
                """,
                (lot_code, limit),
            )

        rows = cur.fetchall()

    # 5. Convert Python datetime objects into JSON-friendly strings.
    for row in rows:
        row["timestamp"] = row["timestamp"].isoformat()

    return jsonify(rows)
