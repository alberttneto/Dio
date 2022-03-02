
/*AULA 01*/

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

/*AULA 01*/
CREATE TABLE videos(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    author INT NOT NULL,
    title VARCHAR(30) NOT NULL,
    likes INT,
    dislikes INT
);


INSERT INTO videos (title, likes, dislikes) VALUES ('PYTHON', 25, 3);
INSERT INTO videos (title, likes, dislikes) VALUES ('CSS', 30, 0);
INSERT INTO videos (title, likes, dislikes) VALUES ('HTML', 29, 3);
INSERT INTO videos (title, likes, dislikes) VALUES ('JavaScript', 15, 10);
INSERT INTO videos (title, likes, dislikes) VALUES ('Java', 5, 0);

CREATE TABLE author(
    id_author INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    nascimento DATE
);

INSERT INTO author (nome, nascimento) VALUES ('João', '1990-05-22');
INSERT INTO author (nome, nascimento) VALUES ('Maria', '1998-07-01');
INSERT INTO author (nome, nascimento) VALUES ('Fatima', '2005-02-22');

UPDATE videos SET author = '1' WHERE id = '1';
UPDATE videos SET author = '2' WHERE id = '2';
UPDATE videos SET author = '3' WHERE id = '3';
UPDATE videos SET author = '2' WHERE id = '4';
UPDATE videos SET author = '1' WHERE id = '5';

ALTER TABLE videos ADD CONSTRAINT fk_author FOREIGN KEY (id_author) REFERENCES author (id_author);

SELECT * FROM videos JOIN author ON videos.author =author.id_author;
SELECT videos.title, author.nome FROM videos JOIN author ON videos.author =author.id_author;

CREATE TABLE seo (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    category VARCHAR(30) NOT NULL
);

INSERT INTO seo (category) VALUES ('front-end');
INSERT INTO seo (category) VALUES ('back-end');

UPDATE videos SET category = '2' WHERE id = '1';
UPDATE videos SET category = '1' WHERE id = '2';
UPDATE videos SET category = '1' WHERE id = '3';
UPDATE videos SET category = '1' WHERE id = '4';
UPDATE videos SET category = '2' WHERE id = '5';

ALTER TABLE videos ADD CONSTRAINT fk_category FOREIGN KEY (id_category) REFERENCES category (id);

SELECT videos.title, seo.category FROM videos JOIN seo ON videos.category = seo.id; 
SELECT videos.title, seo.category, author.nome FROM videos 
    JOIN seo ON videos.category = seo.id
    JOIN author ON videos.author = author.id_author;

CREATE TABLE playlist(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL
);

INSERT INTO playlist (nome) VALUES ('HTML + CSS');
INSERT INTO playlist (nome) VALUES ('HTML + CSS + JAVASCRIPT');
INSERT INTO playlist (nome) VALUES ('JAVA + PYTHON');

CREATE TABLE videos_playlist(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_videos INT NOT NULL,
    id_playlist INT NOT NULL
);

INSERT INTO videos_playlist (id_videos, id_playlist) VALUES ('2','1');
INSERT INTO videos_playlist (id_videos, id_playlist) VALUES ('3','1');
INSERT INTO videos_playlist (id_videos, id_playlist) VALUES ('2','2');
INSERT INTO videos_playlist (id_videos, id_playlist) VALUES ('3','2');
INSERT INTO videos_playlist (id_videos, id_playlist) VALUES ('4','2');
INSERT INTO videos_playlist (id_videos, id_playlist) VALUES ('1','3');
INSERT INTO videos_playlist (id_videos, id_playlist) VALUES ('5','3');

ALTER TABLE videos_playlist ADD CONSTRAINT fk_videos FOREIGN KEY (id_videos) REFERENCES videos (id);
ALTER TABLE videos_playlist ADD CONSTRAINT fk_playlist FOREIGN KEY (id_playlist) REFERENCES playlist (id);

SELECT * FROM playlist JOIN videos_playlist ON playlist.id = videos_playlist.id_playlist
    JOIN videos ON videos.id = videos_playlist.id_videos;



