-- SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed
CREATE TRIGGER change_email BEFORE INSERT ON users
    FOR EACH ROW
    BEGIN
        IF valid_email == 0 THEN
            SET valid_email = 1
            WHERE email = NEW.email
        ELSEIF valid_email == 1 THEN
            SET valid_email = 0
            WHERE email = NEW.email
        END IF;
    END;
