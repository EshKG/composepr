-- Database: postgres

-- DROP DATABASE IF EXISTS postgres;


CREATE TABLE tickets (
    id serial PRIMARY KEY,
    name varchar(40) ,
    secondname varchar(40) ,
    patronymic varchar(40) ,
    phone varchar(40),
    text text
);
