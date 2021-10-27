FROM postgres:latest

ADD init_user_and_db.sql /docker-entrypoint-initdb.d/
