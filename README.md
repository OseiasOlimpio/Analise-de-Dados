# Relatório de Vendas — Superstore

Análise exploratória de dados de vendas com Python (pandas + matplotlib).

## Base de dados
Superstore Sales Dataset (Kaggle) — 9.994 registros de pedidos, 21 colunas, sem valores nulos.

## Como rodar
```bash
pip install -r requirements.txt
python analise.py
```

## Principais resultados

- **Faturamento total:** $2.297.200,86
- **Ticket médio por venda:** $229,86
- **Pedidos únicos:** 5.009

### Sazonalidade
As vendas têm um padrão claro e recorrente: **picos em setembro e novembro**, com queda em janeiro/fevereiro todos os anos analisados (2014–2017). Novembro coincide com a Black Friday e o início da temporada de fim de ano nos EUA. **Recomendação:** reforçar estoque e equipe de vendas nesse período.

### Produtos
- Produto mais vendido em **unidades**: Staples (215 un.)
- Produto que mais fatura: Canon imageCLASS 2200 (~$61.6k) — poucas vendas, mas de alto valor

### Categorias
Technology lidera o faturamento ($836k), seguida de Furniture ($742k) e Office Supplies ($719k). Nas sub-categorias, **Phones** e **Chairs** se destacam.

## Gráficos gerados
- `grafico_vendas_mensais.png`
- `grafico_top5_produtos.png`
