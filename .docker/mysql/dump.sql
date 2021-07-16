CREATE DATABASE kifaco;

use kifaco;

CREATE TABLE diet (
	id TINYINT AUTO_INCREMENT PRIMARY KEY,
    kind VARCHAR(100)
);
select * from diet;
INSERT INTO diet (kind) VALUES
('VEGANO'), ('VEGETARIANO'), ('REDUCETARIANOS'), ('CRUDIVORO'), ('ONIVORO'), ('CARNIVORO')
;

CREATE TABLE household_appliance(
	id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150)
);
INSERT INTO household_appliance(name) VALUES
('FOGAO'), ('MICROONDAS'), ('AIRFRYER'), ('PANELA_DE_PRESSAO'), ('FRIGIDEIRA'), ('FORNO'), ('PANELA')
;

CREATE TABLE ingredients(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    ingredients VARCHAR(150),
    kind ENUM('CEREAIS', 'PAES', 'TUBERCULOS', 'HORTALICAS', 'FRUTAS', 'LEGUMINOSAS', 'CARNE', 'OVOS', 'DERIVADOS DO LEITE', 'OLEO', 'GORDURA'),
    KEY (ingredients)
);
INSERT INTO ingredients (ingredients, kind) VALUES
('ARROZ', 'CEREAIS'), ('FEIJAO', 'LEGUMINOSAS'), ('COUVE FLOR', 'HORTALICAS'), ('BERINGELA', 'HORTALICAS'), ('KIABO', 'HORTALICAS')
;

CREATE TABLE types_meal(
	id TINYINT AUTO_INCREMENT PRIMARY KEY,
    meal VARCHAR(100)
);
INSERT INTO types_meal(meal) VALUES
('CAFE_DA_MANHA'), ('ALMOCO'), ('CAFE_DA_TARDE'), ('JANTAR'), ('CEIA'), ('SOBREMESA'), ('EXODICO'), ('ESTRANGEIRA')
;

CREATE TABLE menu(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    diet TINYINT,
    types_meal TINYINT,
    plate VARCHAR(150),
    calorie INT,
    time TIME,
    complement JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL DEFAULT NULL,
    KEY (plate),
    KEY (calorie),
    KEY (time),
    FOREIGN KEY (types_meal) REFERENCES types_meal(id),
    FOREIGN KEY (diet) REFERENCES diet(id)
);
INSERT INTO menu(types_meal, diet, plate, calorie, time) VALUES
(2, 1, 'Legumes e Verdura', 200, '15:00')
;

CREATE TABLE menu_x_ingredients(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    menu BIGINT,
    ingredients BIGINT,
    amount INT,
    unit_of_measurement ENUM('GRAMAS', 'COLHER_SOPA', 'COPO_CHA', 'COLHER_SOBREMESA', 'COPO_CAFE', 'ML', 'KG', 'UNIDADE', 'XICARA'),
    FOREIGN KEY (menu) REFERENCES menu(id),
    FOREIGN KEY (ingredients) REFERENCES ingredients(id)
);
INSERT INTO menu_x_ingredients (menu, ingredients, amount, unit_of_measurement) VALUES
(1, 1, 2, 'XICARA'),
(1, 2, 1, 'XICARA'),
(1, 4, 1, 'UNIDADE'),
(1, 5, 5, 'UNIDADE')
;

CREATE TABLE user(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    diet TINYINT,
    name VARCHAR(250),
    password VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL DEFAULT NULL,
    KEY(created_at),
    FOREIGN KEY (diet) REFERENCES diet(id)
);
INSERT INTO user (diet, name) VALUES(6, 'Leon Okubo de Souza');

CREATE TABLE user_x_menu(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user BIGINT,
    menu BIGINT,
    FOREIGN KEY (user) REFERENCES user(id),
    FOREIGN KEY (menu) REFERENCES menu(id)
);
INSERT INTO user_x_menu(user, menu) VALUES (1, 1);

CREATE TABLE user_x_household_appliance(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user BIGINT,
    household_appliance SMALLINT,
    FOREIGN KEY (user) REFERENCES user(id),
    FOREIGN KEY (household_appliance) REFERENCES household_appliance(id)
);
INSERT INTO user_x_household_appliance (user, household_appliance) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7);

CREATE TABLE blacklist(
	id INT AUTO_INCREMENT PRIMARY KEY,
    user BIGINT,
    ingredients BIGINT,
    FOREIGN KEY (user) REFERENCES user(id),
    FOREIGN KEY (ingredients) REFERENCES ingredients(id)
);

CREATE TABLE to_cook(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    menu BIGINT,
    cook TEXT,
    FOREIGN KEY (menu) REFERENCES menu(id)
);
INSERT INTO to_cook(menu, cook) VALUES (1, 'COZINHAR TUDO NA PRESAO POR 10 minutos e GG');
