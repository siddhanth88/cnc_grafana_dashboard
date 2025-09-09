CREATE TABLE spindle_data (
    id SERIAL PRIMARY KEY,
    time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    machine TEXT NOT NULL,
    spindle_speed INTEGER,
    power_state TEXT,
    is_anomaly BOOLEAN DEFAULT FALSE,   -- anomaly flag
    anomaly_score FLOAT                 -- optional: score from model
);
