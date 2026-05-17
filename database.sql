CREATE DATABASE hotelaria;
USE hotelaria;

CREATE table hospedes (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NULL,
    telefone VARCHAR(20) NULL,
    cpf VARCHAR(14) UNIQUE
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

INSERT INTO hospedes(nome, email, telefone, cpf) VALUES ("Guilherme Ballestrim", "gui.bs@outlook.com", "11921886001", "46776989885");

INSERT INTO reservas(hospede_id, quarto_id, data_entrada, data_saida)
VALUES(
    16,
    4,
    16-04-2026,
    20-04-2026
);

SELECT * FROM reservas;