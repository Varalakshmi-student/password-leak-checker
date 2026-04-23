DELIMITER //
CREATE PROCEDURE CheckPassword(IN p_hash VARCHAR(64))
BEGIN
    SELECT COUNT(*) AS is_leaked, source
    FROM leaked_passwords
    WHERE password_hash = p_hash
    GROUP BY source;
END //
DELIMITER ;