CREATE TABLE pessoa (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    nascimento DATE
);

INSERT INTO pessoa (nome, nascimento) VALUES ('Jõao', '1993-04-23');
INSERT INTO pessoa (nome, nascimento) VALUES ('Maria', '1990-12-01');
INSERT INTO pessoa (nome, nascimento) VALUES ('Sophia', '2000-05-03');

UPDATE pessoa SET nome = 'Julio' WHERE id = '1';
UPDATE pessoa SET genero = 'M' WHERE id = '1';
UPDATE pessoa SET genero = 'F' WHERE id = '3';
UPDATE pessoa SET genero = 'F' WHERE id = '4';

ALTER TABLE pessoa ADD genero VARCHAR(1) NOT NULL AFTER nascimento;

SELECT * FROM pessoa;

DELETE FROM pessoa WHERE id = '2';

SELECT * FROM pessoa ORDER BY nome;

SELECT * FROM pessoa ORDER BY nome DESC;

SELECT COUNT(id), genero FROM pessoa GROUP BY genero;


