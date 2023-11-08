DELIMITER //

CREATE PROCEDURE RemoveInactiveMentors()
BEGIN
    DECLARE cutoff_date DATETIME;
    SET cutoff_date = NOW() - INTERVAL 180 DAY;
    
    -- Delete mentors who are not approved and have a last_application_date greater than the cutoff date
    DELETE FROM mentor
    WHERE approved = 0 AND last_application_date < cutoff_date;
    
END;

//

DELIMITER ;
