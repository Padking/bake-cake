CREATE USER <имя П-ля, НЕ обладающего правами суперпользователя с т.зр. БД> WITH ENCRYPTED PASSWORD '<пароль>';
CREATE DATABASE <имя БД> ENCODING 'UTF8' template=template0 OWNER <имя П-ля, НЕ обладающего правами суперпользователя с т.зр. БД>;
GRANT ALL PRIVILEGES ON DATABASE <имя БД> TO <имя П-ля, НЕ обладающего правами суперпользователя с т.зр. БД>;
