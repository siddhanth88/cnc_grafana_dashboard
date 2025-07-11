CREATE TABLE spindle_data (
    time TIMESTAMPTZ NOT NULL,
    machine TEXT NOT NULL,
    spindle_speed INTEGER,
    power_state TEXT
);
