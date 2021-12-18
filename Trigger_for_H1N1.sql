DELIMITER $$
CREATE TRIGGER H1N1_concern_trigger BEFORE INSERT ON e2e.H1N1
FOR EACH ROW
BEGIN 
IF NEW.H1N1_concern <=3 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'H1N1 concern should be a numerical value between 0 and 3. Please try again.'
;END IF;
END; $$