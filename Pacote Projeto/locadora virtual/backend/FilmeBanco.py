import psycopg2
from backend.Filme import Filme

class FilmeBanco:

    def get_all_filmes(self, atributo):

        db_connection = psycopg2.connect(dbname='locadora',
                                         user="postgres",
                                         password="eduar26",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()
        cmd_sql = "SELECT " + atributo + " FROM filme;"
        print(cmd_sql)

        db_cursor.execute(cmd_sql)
        lista_filmes  = db_cursor.fetchall()
        db_connection.commit()
        db_connection.close()

        lista_filmes_resposta = []
        
        for filme_banco in lista_filmes:
            
            id = filme_banco[0]
            nome   = filme_banco[1]
            ano  = filme_banco[2]
            classificacao   = filme_banco[3]
            username = filme_banco[4]

            filme_item = Filme(id,nome, ano, classificacao, username)
            lista_filmes_resposta.append(filme_item)
            
        return lista_filmes_resposta


    def insert_new_filme(self,nome, ano, classificacao, username):
        db_connection = psycopg2.connect(dbname='locadora',
                                         user="postgres",
                                         password="eduar26",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()
        cmd_sql = "INSERT INTO filme (nome_filme, ano_filme, classificacao_filme, username) VALUES (%s, %s, %s, %s);"
        valores = (nome, ano, classificacao, username)

        try:
            db_cursor.execute(cmd_sql, valores)
            db_connection.commit()
            print("Filme inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir filme: {e}")
        finally:
            db_connection.close()
            
    def update_filme(self, id_filme, novo_nome, novo_ano, nova_classificacao):
        
        db_connection = psycopg2.connect(dbname='locadora',
                                        user="postgres",
                                        password="eduar26",
                                        host='localhost',
                                        port=5432)
        db_cursor = db_connection.cursor()

        cmd_sql = """
            UPDATE filme 
            SET nome_filme = %s, ano_filme = %s, classificacao_filme = %s
            WHERE id_filme = %s;
        """
        
        valores = (novo_nome, novo_ano, nova_classificacao,id_filme)

        try:

            db_cursor.execute(cmd_sql, valores)
            db_connection.commit()
            print("Filme atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar filme: {e}")
        finally:
            db_connection.close()
            
    def delete_filme(self, id):
        db_connection = psycopg2.connect(dbname='locadora',
                                        user="postgres",
                                        password="eduar26",
                                        host='localhost',
                                        port=5432)
        db_cursor = db_connection.cursor()
        
        cmd_sql = """
            DELETE FROM filme 
            WHERE id_filme = %s;
        """
        
        valores = (id,)
        
        try:
            db_cursor.execute(cmd_sql, valores)
            db_connection.commit()
            print("Filme removido com sucesso!")
        except Exception as e:
            print(f"Erro ao remover filme: {e}")
        finally:
            db_connection.close()
    
def teste_filme():
    
    filme_banco = FilmeBanco()
    
    '''id = 2
    
    print("\nFilme removido...")
    filme_banco.delete_filme(id)

    # Verificando os filmes após a atualização
    print("\nFilmes após a atualização:")'''
    
    nome = "Inception"
    ano = "2010"
    classificacao = "14"
    username = "carlosalmeida"
    
    print("Inserindo novo filme...")
    filme_banco.insert_new_filme(nome, ano, classificacao, username)

    filmes = filme_banco.get_all_filmes("*")
    for filme in filmes:
        print(f"Id: {filme.get_id()}, Nome: {filme.nome}, Ano: {filme.ano}, Classificação: {filme.classificacao}, Senha: {filme.username}")
   
    '''
    filmes = filme_banco.get_all_filmes("*")
    for filme in filmes:
        print(f"Nome: {filme.get_nome()}, Ano: {filme.ano}, Classificação: {filme.classificacao}, Senha: {filme.senha_usuario}")
    
    print("Recuperando todos os filmes...")
    filmes = filme_banco.get_all_filmes("*") # Selecionando todos os atributos do filme
    
    # Mostrando os filmes recuperados
    for filme in filmes:
        print(f"Nome: {filme.get_nome()}, Ano: {filme.ano}, Classificação: {filme.classificacao}, Senha: {filme.senha_usuario}") '''
    
    
    
        