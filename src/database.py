import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()


# Cria uma nova conexão com o banco MySQL
def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
    )


def salvar_historico(pokemon):
    cursor = None
    conexao = None
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO historico_pesquisas (pokemon) VALUES (%s)",
            (pokemon,)
        )

        conexao.commit()

    except mysql.connector.Error as erro:
        print(erro)

    finally:
        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def mostrar_historico():
    
    cursor = None
    conexao = None
    
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM historico_pesquisas"
        )

        resultado = cursor.fetchall()
        return resultado

    except mysql.connector.Error as erro:
        print(erro)
        return []

    finally:
        if cursor:
            cursor.close()

        if conexao:
            conexao.close()