-- Sanitized example schema for a parking availability application.
-- Demonstrates time-series occupancy data, contextual calendar data,
-- and application announcements.

-- Table containing parking lot data.
CREATE TABLE IF NOT EXISTS occupancy_readings (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    lot_code TEXT NOT NULL,
    availability_percent REAL NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_location_timestamp
    ON occupancy_readings (location_code, timestamp);

-- Table containing context for training the forecasting model.
CREATE TABLE IF NOT EXISTS calendar_context (
    date DATE PRIMARY KEY,
    is_exam_period BOOLEAN NOT NULL DEFAULT FALSE,
    is_class_in_session BOOLEAN NOT NULL DEFAULT TRUE,
    -- Other context points hidden.
);

-- Table for controlling in-app annoucements.
CREATE TABLE IF NOT EXISTS announcements (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT NOT NULL,
    urgency TEXT NOT NULL DEFAULT 'generic',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_dismissible BOOLEAN NOT NULL DEFAULT TRUE,
    starts_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    date_created TIMESTAMPTZ NOT NULL DEFAULT now(),
    date_updated TIMESTAMPTZ NOT NULL DEFAULT now(),
    author TEXT

);
