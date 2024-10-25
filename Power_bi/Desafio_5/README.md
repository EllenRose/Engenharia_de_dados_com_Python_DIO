# Desafio Prático:Modelando um Dashboard de e-commerce com Power bi , utilizando fórmula DAX

**Objetivo:** Á Partir da tabela base que a professora disponilizou , deveriam ser criado tabelas dimensões e fato , baseado no esquema estrela(Star Schema) e utilizando a fórmula DAX , foi feito a criação da tabela dimensão calendário.

Fórmula DAX utilizada para a criação da tabela calendário:
- Criação da tabela d_calendario = CALENDARAUTO()
- Criação da coluna Ano YEAR= YEAR('d_calendario'[Date])
- Criação da coluna dia da semana = WEEKNUM('d_calendario'[Date])
- Criação da coluna Mês = MONTH('d_calendario'[Date]) 
- Criação da coluna de trimestre = QUARTER('d_calendario'[Date])

  **Tabelas Criadas á partir da cópia  da base financials** :
  
  Tabela Fato:
- fVendas (SK_ID , ID_Produto, Produto, Units Sold, Sales Price, Discount Band, Segment, Country, Salers, Profit)

  Tabelas dimensões:
- dDescontos (ID_produto, Discount, Discount Band)
- dDetalhes (ID_produto, Segment, Country, Profit, CGOS, SK_ID)
- dProdutos (ID_produto, Produto, Média de Unidades Vendidas, Médias do valor de vendas, Mediana do valor de vendas, Valor máximo de Venda, Valor mínimo de Venda)
- dDetalhes_produtos (ID_produtos, Discount Band, Sale Price, Units Sold, Manufactoring Price)
- dCalendario ( Data, ano , mes, dia da semana e trimestre).
  
