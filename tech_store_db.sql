-- Crear tabla de productos
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    stock INTEGER NOT NULL,
    image_url VARCHAR(255)
);

-- Crear tabla de clientes
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);



INSERT INTO product (name, description, price, stock, image_url) VALUES
('Laptop Gamer X1000', 'High-performance laptop for gaming.', 1500.00, 10, 'https://via.placeholder.com/350x200?text=Laptop+Gamer+X1000'),
('Mouse Pro', 'Ergonomic wireless mouse.', 25.99, 50, 'https://via.placeholder.com/350x200?text=Mouse+Pro'),
('Teclado Mecánico RGB', 'Mechanical keyboard with RGB backlight.', 75.50, 30, 'https://via.placeholder.com/350x200?text=Teclado+RGB');


INSERT INTO customer (name, email) VALUES
('John Doe', 'johndoe@example.com'),
('Jane Smith', 'janesmith@example.com');
