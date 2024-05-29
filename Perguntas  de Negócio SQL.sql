# 1  Qual montante de transações do mês? 

SELECT SUM(CAST(REPLACE(montantetransacao, 'R$', '') AS FLOAT)) AS Total_Abril
FROM transacoes;

# 2 Quantas transações por tipo foram realizadas? 
SELECT tipotransacao, COUNT(*) AS numerotransacoes
FROM transacoes
GROUP BY tipotransacao;

# 3 Qual montante de movimentações por cliente? 
SELECT c.nomecliente, SUM(CAST(REPLACE(t.montantetransacao,'R$', '' )AS FLOAT)) AS total_de_abril_por_cliente
FROM transacoes t
JOIN dados_clientes c ON t.idcliente = c.idcliente
GROUP BY c.nomecliente;

# 4 Qual montante  por região? 
SELECT c.região, SUM(CAST(REPLACE(t.montantetransacao, 'R$', '') AS FLOAT)) AS Total_por_região
FROM transacoes t
JOIN dados_clientes c ON t.idcliente = c.idcliente
GROUP BY c.região;







