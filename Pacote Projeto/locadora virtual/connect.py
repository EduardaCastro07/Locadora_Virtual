import psycopg2
from config import load_config


def connect(config):
    
    try:
        conn = psycopg2.connect(**config)
        print('Connected to the PostgreSQL server.')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return None  
    
def query_data(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario;")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def teste_connect():
    config = load_config()
    conn = connect(config) 

    if conn:  
        query_data(conn)  
        
    conn.close()  

'''def insert_usuario(conn, nome, email):
    """ Insere um novo usuário na tabela usuario """
    try:
        # Cria um cursor para executar comandos SQL
        with conn.cursor() as cursor:
            # Escreve o comando de inserção
            sql = "INSERT INTO usuario (username, senha) VALUES (%s, %s)"
            # Executa o comando de inserção com os valores
            cursor.execute(sql, (nome, email))
            # Confirma a transação
            conn.commit()
            print('Usuário adicionado com sucesso.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(f'Erro ao inserir usuário: {error}')
        conn.rollback()  # Desfaz a transação em caso de erro
    
    if conn:
        # Exemplo de inserção de usuário
        insert_user(conn, 'João Silva', '874456')

        # Fecha a conexão ao banco de dados
        conn.close()
'''





