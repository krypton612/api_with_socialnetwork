CREATE TABLE pages(
    id_page INT PRIMARY KEY 
);

CREATE TRIGGER ver1user ON tb_notes FOR Insert
AS
if select id_user_fk from inserted < 2
Begin
    print 'escoja otro usuario'
    RollBack
END;

       
       CREATE TRIGGER upd_check BEFORE INSERT ON tb_notes
       FOR EACH ROW
       BEGIN
           IF NEW.amount < 0 THEN
               SET NEW.amount = 0;
           ELSEIF NEW.amount > 100 THEN
               SET NEW.amount = 100;
           END IF;
       END;//

        CREATE TRIGGER tg1 BEFORE INSERT ON tb_notes
        FOR EACH ROW
        BEGIN
            IF NEW.id_user_fk < 1
                RollBack;
        END;//


       CREATE TRIGGER inst_check BEFORE UPDATE ON tb_notes
       FOR EACH ROW
       BEGIN
           IF NEW.id_user_fk < 2 THEN
               PRINT 'PERRA';
           END IF;
       END;//


-- la forma de crear un trigger con condicionales

DELIMITER //
    CREATE TRIGGER tb_check AFTER INSERT ON tb_notes
    FOR EACH ROW
    BEGIN
        IF (select count(id_page_fk) from tb_notes where id_page_fk=NEW.id_page_fk) = 4 THEN
           INSERT INTO tb_pages(id_page) value(null);
        END IF;
    END; //
DELIMITER ;





insert into tb_notes(id_note, content, fecha, id_user_fk, id_page_fk) values(null, "sdadsa", null, 1, 4);

ELSEIF (select count(id_page_fk) from tb_notes) > 5 THEN
            INSERT INTO tb_pages(id_page) value(null);

SELECT n.id_note, u.name, u.lastname, n.content, n.fecha, n.id_page_fk FROM tb_notes n
    INNER JOIN tb_users u
    ON u.id_user = n.id_user_fk
    ORDER BY n.id_note desc


SELECT count(n.id_page_fk) FROM tb_notes n
    INNER JOIN tb_pages u
    ON n.id_page_fk = (select count(id_page) from tb_pages);


select count(id_page_fk) from tb_notes