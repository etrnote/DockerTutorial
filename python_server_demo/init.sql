CREATE TABLE IF NOT EXISTS message (
  id SERIAL PRIMARY KEY,
  content VARCHAR(255) NOT NULL,
  timestamp TIMESTAMP NOT NULL DEFAULT current_timestamp,
  creator VARCHAR(50) NOT NULL
);