CREATE DATABASE hotelaria;
USE hotelaria;

CREATE table hospedes (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(30) NOT NULL,
    email VARCHAR(40) NULL,
    telefone VARCHAR(11) NULL,
    cpf VARCHAR(11) UNIQUE
);

CREATE table quartos (
	id INT PRIMARY KEY AUTO_INCREMENT,
	numero VARCHAR(10) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    valor_diaria DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE table reservas (
	id INT PRIMARY KEY AUTO_INCREMENT,
	hospede_id INT,
    quarto_id INT,
    data_entrada DATE NOT NULL,
    data_saida DATE NOT NULL,
    
    FOREIGN KEY (hospede_id) REFERENCES hospedes(id),
    FOREIGN KEY (quarto_id) REFERENCES quartos(id)
);

INSERT INTO hospedes(nome, email, telefone, cpf)
VALUES
('João Silva', 'joao@email.com', '11999999999', '111.111.111-11'),
('Maria Souza', 'maria@email.com', '11888888888', '222.222.222-22');

INSERT INTO quartos(numero, tipo, valor_diaria, status)
VALUES
('101', 'Solteiro', 120.00, 'Disponível'),
('102', 'Casal', 180.00, 'Ocupado'),
('201', 'Luxo', 350.00, 'Manutenção');

INSERT INTO reservas(hospede_id, quarto_id, data_entrada, data_saida)
VALUES
(1, 2, '2026-05-10', '2026-05-15');
