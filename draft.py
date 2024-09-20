import pandas as pd
import sqlite3

from functions.create_db import create_db
from functions.drop_table import drop_table
from functions.create_table import create_table
from functions.insert_rows import insert_one_row

conn= sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

colums_desc ="""
    id_cliente INT PRIMARY KEY ,
    nome TEXT
"""
create_db('mydatabase')

create_table(
    database='mydatabase',
    table_name='Cliente',
    columns_desc= colums_desc
)

create_table(database='mydatabase',
             table_name='Cliente',
             columns_desc="""
             id_cliente INTEGER PRIMARY KEY,
             nome_completo CHAR NOT NULL,
             idade INTEGER NOT NULL,
             CPF CHAR NOT NULL,
             telefone CHAR,
             endereco CHAR NOT NULL,
             animal_preferido CHAR,
             saldo_bancario FLOAT NOT NULL,
             ultima_aposta CHAR NOT NULL""")

data = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4],
    'nome_completo': ['Alice', 'Bob', 'Charlie', 'David'],
    'idade': [64, 25, 66, 15],
    'CPF': ['154156458-45', '789456123-78', '456798123-56', '123456789-74'],
    'telefone': ['741852963', '789456123', '963852741', '753951852'],
    'endereco': ['rua silvinha', 'rua Samuel', 'rua Macedo', 'rua Heloisa'],
    'animal_preferido': ['Alce', 'Cobra', 'Cavalo', 'Cachorro'],
    'saldo_bancario': [798.8, 5.5, 89.5, 9000.7],
    'ultima_aposta': ['20-08-2017', '12-07-2019', '25-09-2019', '12-07-2024']
})

data.to_sql(
    'Cliente', conn,
    if_exists='replace',
    index=False
)

create_table(database='mydatabase',
             table_name='Operador',
             columns_desc="""
             id_operador INTEGER PRIMARY KEY,
             nome_completo CHAR NOT NULL,
             nome_de_usuario CHAR NOT NULL,
             senha CHAR NOT NULL,
             funcao CHAR NOT NULL""")

data = pd.DataFrame({
    'id_operador': [1, 2, 3, 4],
    'nome_completo': ['Carlos Silva', 'Ana Souza', 'João Pereira', 'Maria Oliveira'],
    'nome_de_usuario': ['csilva', 'asouza', 'jpereira', 'moliveira'],
    'senha': ['senha123', 'senha456', 'senha789', 'senha012'],
    'funcao': ['Gerente', 'Analista', 'Suporte', 'Desenvolvedor']
})

data.to_sql(
    'Operador', conn,
    if_exists='replace',
    index=False
)

create_table(database='mydatabase',
             table_name='Aposta',
             columns_desc="""
             id_aposta INTEGER PRIMARY KEY,
             id_cliente INTEGER,
             id_operador INTEGER,
             data_aposta CHAR NOT NULL,
             saldo_aposta CHAR NOT NULL,
             escolha_animal_aposta CHAR NOT NULL,
             status CHAR NOT NULL,
             ultima_aposta CHAR,
             FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
             FOREIGN KEY (id_operador) REFERENCES Operador(id_operador)
             """)

data = pd.DataFrame({
    'id_aposta': [101, 102, 103, 104],
    'id_cliente': [1, 2, 3, 4],  # IDs de cliente que devem existir na tabela Cliente
    'data_aposta': ['01-10-2023', '02-10-2023', '05-03-2023', '04-01-2023'],
    'saldo_aposta': ['100', '200', '300', '400'],
    'escolha_animal_aposta': ['Cavalo', 'Cachorro', 'Cobra', 'Alce'],
    'status': ['Concluído', 'Concluído', 'Pendente', 'Cancelado'],
    'ultima_aposta': ['01-10-2023', '02-10-2023', '05-03-2023', '04-01-2023']
})

# Insira os dados na tabela Aposta
data.to_sql(
    'Aposta', conn,
    if_exists='replace',
    index=False
)



create_table(database='mydatabase',
             table_name='Pagamentos',
             columns_desc="""
             id_pagamento INTEGER PRIMARY KEY,
             id_aposta INTEGER,
             qtd_pagamento FLOAT NOT NULL,
             data_pagamento CHAR,
             FOREIGN KEY (id_aposta) REFERENCES Aposta(id_aposta)
             """)

data = pd.DataFrame({
    'id_pagamento': [1, 2, 3, 4],
    'id_aposta': [101, 102, 103, 104],  # Esses IDs precisam existir na tabela Aposta
    'qtd_pagamento': [500.0, 150.75, 800.60, 300.25],
    'data_pagamento': ['15-01-2023', '20-02-2023', '03-10-2023', '04-05-2023']
})

# Insira os dados na tabela Pagamentos
data.to_sql(
    'Pagamentos', conn,
    if_exists='replace',
    index=False
)


create_table(database='mydatabase',
             table_name='Executor',
             columns_desc="""
             id_executor INTEGER PRIMARY KEY,
             vulgo CHAR NOT NULL,
             telefone CHAR,
             endereco CHAR
             """)

data = pd.DataFrame({
    'id_executor': [1, 2, 3, 4],
    'vulgo': ['Toninho', 'Pedreira', 'Alirio', 'Rompe_Vaso'],
    'telefone': ['998877665', '998877662', '998877663', '998877664'],
    'endereco': ['Rua A', 'Rua B', 'Rua C', 'Rua D']
})

data.to_sql(
    'Executor', conn,
    if_exists='replace',
    index=False
)

drop_table(
    database='mydatabase',
    table_name='cliente'
)

cursor.execute("""
    DROP TABLE produto
               """)

query = """ 
    SELECT Name 
    FROM client
    WHERE name IN ('Alice', 'David')
"""