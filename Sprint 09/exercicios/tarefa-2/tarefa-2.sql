-- View Dimensão Cliente
CREATE VIEW Dim_Cliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_cliente;

-- View Dimensão Carro
CREATE VIEW Dim_Carro AS
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel, tipoCombustivel
FROM tb_carro;

-- View Dimensão Vendedor
CREATE VIEW Dim_Vendedor AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_vendedor;

-- View Fato Locacao
CREATE VIEW Fato_Locacao AS
SELECT L.idLocacao, L.idCliente, L.idCarro, L.idVendedor, L.dataLocacao, L.qtdDiaria, L.vlrDiaria, L.dataEntrega
FROM tb_locacao L;

