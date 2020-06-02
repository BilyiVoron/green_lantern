-- DROP DATABASE inspection_db;
--
-- CREATE DATABASE inspection_db;


-- CREATE USER inspection_user WITH ENCRYPTED PASSWORD 'inspection_user';


-- GRANT ALL PRIVILEGES ON DATABASE inspection_db TO inspection_user;


CREATE TABLE Country (
    country_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL
    );


CREATE TABLE City (
    city_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL,
    country_id INT REFERENCES Country(country_id) ON DELETE CASCADE
    );


CREATE TABLE Season (
    season_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(30) NOT NULL
    );


CREATE TABLE Dish (
    dish_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(100) UNIQUE NOT NULL,
    ingredients VARCHAR(255),
    recipe VARCHAR(255),
    weight INT CHECK(Weight > 0) NOT NULL,
    price DECIMAL,
    season_id INT REFERENCES Season(season_id) ON DELETE CASCADE
    );

CREATE TABLE Menu (
    menu_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    dish_id INT REFERENCES Dish(dish_id) ON DELETE RESTRICT
    );


CREATE TABLE Restaurant (
    restaurant_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INT REFERENCES Country(country_id),
    city_id INT REFERENCES City(city_id),
    address CHAR(100) NOT NULL UNIQUE,
    menu_id INT REFERENCES Menu(menu_id)
    );


CREATE TABLE Employee (
	employee_id SERIAL PRIMARY KEY,
	position VARCHAR(50) NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	birth_date DATE,
	address CHAR(100) NOT NULL,
	country_id INT REFERENCES Country(country_id),
    city_id INT REFERENCES City(city_id),
	phone_no INT NOT NULL,
	restaurant_id INT REFERENCES Restaurant(restaurant_id) ON DELETE CASCADE
	);
