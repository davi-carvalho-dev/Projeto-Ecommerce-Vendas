import pandas as pd

# -------------------------------------------------------------
# PASSO 1: Gerar o arquivo CSV bruto no seu computador
# -------------------------------------------------------------
dados_brutos = {
    'id_pedido': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'data_venda': ['2024-01-15', '2024-01-16', '17/01/2024', '2024-01-18', '2024-01-19', '2024-01-20', '2024-01-20', '2024-01-21', '2024-01-22'],
    'cliente_id': ['C101', 'C102', 'C103', 'C104', 'C105', 'C106', 'C106', 'C107', 'C108'],
    'categoria': ['Eletrônicos', 'Vestiário', 'Eletrônicos', 'Casa', 'Vestiário', 'Eletrônicos', 'Eletrônicos', None, 'Casa'],
    'preco_unitario': [1500.0, 80.0, 350.0, 120.0, 200.0, 800.0, 800.0, 50.0, 300.0],
    'quantidade': [1, 2, 1, 3, None, 1, 1, 4, 2]
}

# Converte o dicionário para DataFrame e salva no arquivo local 'vendas_ecommerce_bruto.csv'
df_gerador = pd.DataFrame(dados_brutos)
df_gerador.to_csv('vendas_ecommerce_bruto.csv', index=False)
print("Arquivo 'vendas_ecommerce_bruto.csv' criado no seu computador!\n")

# -------------------------------------------------------------
# PASSO 2: Ler o arquivo CSV criado e explorar a tabela
# -------------------------------------------------------------
df_ecommerce = pd.read_csv('vendas_ecommerce_bruto.csv')

# Exibindo as primeiras 5 linhas
print("\n")
print("--- Primeiras linhas da tabela (head) ---")
print(df_ecommerce.head())

# Exibindo o resumo estrutural da tabela
print("\n--- Informações técnicas da tabela (info) ---")
print(df_ecommerce.info())

print("\n--- Quantidade de Nulos nas tabelas ---")
print(df_ecommerce.isna().sum())

print("\n")
df_ecommerce['categoria'] = df_ecommerce["categoria"].fillna("Outros")
df_ecommerce['quantidade'] = df_ecommerce["quantidade"].fillna("1.0")
print(df_ecommerce)

df_ecommerce['data_venda'] = pd.to_datetime(df_ecommerce['data_venda'], format='mixed')

# Contar quantas linhas duplicadas existem na tabela
colunas_checar = ['data_venda', 'cliente_id', 'categoria', 'preco_unitario', 'quantidade']
print(f"Duplicatas encontradas: {df_ecommerce.duplicated(subset=colunas_checar).sum()}")
df_ecommerce = df_ecommerce.drop_duplicates(subset=colunas_checar)

# Remover as linhas duplicadas mantendo apenas a primeira ocorrência
df_ecommerce = df_ecommerce.drop_duplicates()

# Criando a coluna de faturamento total do pedido
df_ecommerce['preco_unitario'] = pd.to_numeric(df_ecommerce['preco_unitario'], errors='coerce')
df_ecommerce['quantidade'] = pd.to_numeric(df_ecommerce['quantidade'], errors='coerce')
df_ecommerce['faturamento_total'] = df_ecommerce['preco_unitario'] * df_ecommerce['quantidade']

# Criação de um novo CSV limpo
df_ecommerce.to_csv('vendas_ecommerce_limpo.csv', index=False)
print('\n')
print(df_ecommerce.info())
print('\n')
print(df_ecommerce)