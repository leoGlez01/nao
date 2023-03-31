use naodatabase;

CREATE TABLE menu(
CODIGO INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
TIPO VARCHAR(50) NOT NULL,
PRODUCTO VARCHAR(50) NOT NULL,
PRECIO FLOAT NOT NULL
);

INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Croquetas Serrano', 489);
INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Croquetas Queso Azul', 459);
INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Croquetas Boloñesa', 399);
INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Empanada Queso Chorizo', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Empanada Boloñesa', 369);
INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Frituras de Malanga', 299);
INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Crema de Calabaza', 389);
INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Tabla de Queso', 699);
INSERT INTO menu (tipo, producto, precio) VALUES ('Entrando en confianza', 'Tabla de Serrano y Queso', 1129);

INSERT INTO menu (tipo, producto, precio) VALUES ('Hablemos de negocio', 'Pulpo Salteado', 1129);
INSERT INTO menu (tipo, producto, precio) VALUES ('Hablemos de negocio', 'Camaron Salteado', 1129);
INSERT INTO menu (tipo, producto, precio) VALUES ('Hablemos de negocio', 'Camaron Tropical', 1199);
INSERT INTO menu (tipo, producto, precio) VALUES ('Hablemos de negocio', 'Pechuga', 1129);
INSERT INTO menu (tipo, producto, precio) VALUES ('Hablemos de negocio', 'Lechon Asado', 1199);
INSERT INTO menu (tipo, producto, precio) VALUES ('Hablemos de negocio', 'Lomo de Cerdo', 1249);
INSERT INTO menu (tipo, producto, precio) VALUES ('Hablemos de negocio', 'Flamenquines', 1399);
INSERT INTO menu (tipo, producto, precio) VALUES ('Hablemos de negocio', 'Arroz a la Cubana', 759);

INSERT INTO menu (tipo, producto, precio) VALUES ('Algo Sencillo', 'Tacos de Camarones', 669);
INSERT INTO menu (tipo, producto, precio) VALUES ('Algo sencillo', 'Taco la Pastor', 669);
INSERT INTO menu (tipo, producto, precio) VALUES ('Algo Sencillo', 'Sandwich Cubano', 599);

INSERT INTO menu (tipo, producto, precio) VALUES ('De Acomodo', 'Arroz Blanco', 159);
INSERT INTO menu (tipo, producto, precio) VALUES ('De Acomodo', 'Platano Maduro Frito', 159);
INSERT INTO menu (tipo, producto, precio) VALUES ('De Acomodo', 'Potaje', 179);
INSERT INTO menu (tipo, producto, precio) VALUES ('De Acomodo', 'Pure de Papa', 359);
INSERT INTO menu (tipo, producto, precio) VALUES ('De Acomodo', 'Vegetales Salteados', 359);

INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Obispo #1', 509);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Chan Chan', 509);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Guantanamera', 509);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Rico Vacilon', 509);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Sangria', 509);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Gin Tonic', 509);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Cubanito', 509);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Blody Mary', 499);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Piña Colada', 489);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Zombie', 479);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Ron Fashioned', 469);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Mary Pickford', 469);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Daiquiri', 449);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Cubata', 449);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Cuba Libre', 449);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Mojito', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'John Collins', 449);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Ron Collins', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Ron Punch', 449);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Canchanchara', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Caipiroska', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Caipirinha', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Caipirisima', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Screw Driver', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Moscow Mule', 429);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Michelada', 689);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cocteles', 'Chelada', 499);

INSERT INTO menu (tipo, producto, precio) VALUES ('Liquidos', 'Agua Natural', 249);
INSERT INTO menu (tipo, producto, precio) VALUES ('Liquidos', 'Jugos Naturales', 279);
INSERT INTO menu (tipo, producto, precio) VALUES ('Liquidos', 'Refresco Nacional', 309);
INSERT INTO menu (tipo, producto, precio) VALUES ('Liquidos', 'Malta', 319);
INSERT INTO menu (tipo, producto, precio) VALUES ('Liquidos', 'Copa de Vino', 399);
INSERT INTO menu (tipo, producto, precio) VALUES ('Liquidos', 'Cerveza Corona', 479);

INSERT INTO menu (tipo, producto, precio) VALUES ('Cafe', 'Cafe Expresso', 129);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cafe', 'Cafe Cortadito', 159);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cafe', 'Cafe Cappuchino', 199);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cafe', 'Cafe Frappuchino', 369);
INSERT INTO menu (tipo, producto, precio) VALUES ('Cafe', 'Cafe con Leche', 179);

INSERT INTO menu (tipo, producto, precio) VALUES ('Aun no convencido', 'Torreja Tentacion', 179);
INSERT INTO menu (tipo, producto, precio) VALUES ('Aun no convencido', 'Arroz con Leche', 2999);
INSERT INTO menu (tipo, producto, precio) VALUES ('Aun no convencido', 'Crema de Frutas', 299);


SELECT * from menu;


