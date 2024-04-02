-- Altera a tabela tb_locacao
ALTER TABLE tb_locacao 
DROP COLUMN nomeCliente, cidadeCliente, estadoCliente, paisCliente, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel, tipoCombustivel, idVendedor, nomeVendedor, sexoVendedor, estadoVendedor;

-- Cria a tabela tb_carro
CREATE TABLE tb_carro (
    idCarro INT PRIMARY KEY,
    kmCarro FLOAT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro INT,
    idcombustivel INT,
    tipoCombustivel INT
);

-- Cria a tabela tb_cliente
CREATE TABLE tb_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(100),
    estadoCliente VARCHAR(50),
    paisCliente VARCHAR(50)
);

-- Cria a tabela tb_vendedor
CREATE TABLE tb_vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor CHAR(1),
    estadoVendedor VARCHAR(50)
);