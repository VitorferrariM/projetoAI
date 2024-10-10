import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os
import logging

# Configurar o logger para registrar os erros em um arquivo de log
logging.basicConfig(filename='erros.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados validados no PostgreSQL
def salvar_no_postgres(dados: Vendas):
    """
    Função para salvar no postgres
    """
    try:
        # Conexão com o banco de dados usando 'with' para garantir que seja fechado corretamente
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        ) as conn:
            with conn.cursor() as cursor:
                # Inserção dos dados na tabela de vendas
                insert_query = sql.SQL(
                    "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
                )
                cursor.execute(insert_query, (
                    dados.email,
                    dados.data,
                    dados.valor,
                    dados.quantidade,
                    dados.produto.value  # Certifique-se de que 'produto' seja tratado corretamente
                ))
            # Commit para salvar as alterações
            conn.commit()
        
        # Mensagem de sucesso
        st.success("Dados salvos com sucesso no banco de dados!")
    
    except Exception as e:
        # Logar o erro no arquivo de log e exibir a mensagem no Streamlit
        logging.error(f"Erro ao salvar no banco de dados: {e}")
        st.error(f"Erro ao salvar no banco de dados: {e}")
