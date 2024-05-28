import pandas as pd #importando pandas para ler o csv
from sqlalchemy import create_engine #importando o sqlalchemy para criar a conexão do banco
try:
    df = pd.read_csv('dados_clientes.csv', encoding='utf-8') #tenta ler o .csv do arquivo dentro do projeto, com o encoding utf-8
except UnicodeDecodeError:
    try:
        df = pd.read_csv('dados_clientes.csv', encoding='latin-1') #tenta ler o .csv do arquivo dentro do projeto, com o encoding latin1
    except UnicodeDecodeError:
        df = pd.read_csv('dados_clientes.csv', encoding='cp1252') #tenta ler o .csv do arquivo dentro do projeto, com o encoding cp1252
        ##Essas tentativas, é para garantir incluir os dados sem problema de caracteres
engine = create_engine('postgresql://postgres:pipoca@localhost:5432/meu_banco_de_dados') 
##valores da string de conexão
##create_engine('TECNOLOGIA://USUARIO:SENHADOUSUARIO@IP:PORTA/DATABASENAME')
        ## TECNOLOGIA : postgres
        ## USUARIO: postgres 
        ## SENHA : senha (sim, a senha criada foi 'senha')
        ## IP : localhost (ja que é um banco criado no docker dentro da minha maquina)
        ## PORTA: 5432 (porta padrão postgres)
        ## DATABASENANE : meu_banco_de_dados     
df.to_sql('dados_clientes', con=engine, if_exists='append', index=False) 
        ##Nome da table 
                         ## ????
                                    ## if_exists= 'append' (se existir a tabela, fazer append(inclusão))
                                                        ##index = falso (caso a tabela não exista), criar no banco