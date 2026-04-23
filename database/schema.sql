CREATE TABLE leaked_passwords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password_hash VARCHAR(64) NOT NULL,
    source VARCHAR(100),
    leaked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE INDEX unique_hash (password_hash)
    );