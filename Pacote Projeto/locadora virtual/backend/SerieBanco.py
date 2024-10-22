import psycopg2
from backend.Serie import Serie

class SerieBanco:

    def get_all_series(self, atributo):

        db_connection = psycopg2.connect(dbname='locadora',
                                         user="postgres",
                                         password="eduar26",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()
        cmd_sql = "SELECT " + atributo + " FROM serie;"
        print(cmd_sql)

        db_cursor.execute(cmd_sql)
        lista_series  = db_cursor.fetchall()
        db_connection.commit()
        db_connection.close()

        lista_series_resposta = []
        
        for serie_banco in lista_series:
            
            id = serie_banco[0]
            nome   = serie_banco[1]
            ano  = serie_banco[2]
            classificacao   = serie_banco[3]
            temporadas = serie_banco[4]

            serie_item = Serie(id,nome, ano, classificacao, temporadas)
            lista_series_resposta.append(serie_item)
           
        return lista_series_resposta

    def insert_new_serie(self, nome, ano, classificacao,temporadas):
        db_connection = psycopg2.connect(dbname='locadora',
                                         user="postgres",
                                         password="eduar26",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()
        cmd_sql = "INSERT INTO serie (nome_serie, ano_serie, classificacao_serie, temporadas) VALUES (%s, %s, %s,%s);"
        valores = (nome, ano, classificacao, temporadas)

        try:
            db_cursor.execute(cmd_sql, valores)
            db_connection.commit()
            print("Serie inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir serie: {e}")
        finally:
            db_connection.close()
            
    def update_serie(self, id_serie, novo_nome, novo_ano, nova_classificacao, nova_temporadas):
      
        db_connection = psycopg2.connect(dbname='locadora',
                                        user="postgres",
                                        password="eduar26",
                                        host='localhost',
                                        port=5432)
        db_cursor = db_connection.cursor()

        cmd_sql = """
            UPDATE serie
            SET nome_serie = %s, ano_serie = %s, classificacao_serie = %s, temporadas = %s
            WHERE id_serie = %s;
        """
        
        valores = (novo_nome, novo_ano, nova_classificacao,nova_temporadas,id_serie)

        try:
            db_cursor.execute(cmd_sql, valores)
            db_connection.commit()
            print("Serie atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar serie: {e}")
        finally:
            db_connection.close()
            
    def delete_serie(self, id):
        db_connection = psycopg2.connect(dbname='locadora',
                                        user="postgres",
                                        password="eduar26",
                                        host='localhost',
                                        port=5432)
        db_cursor = db_connection.cursor()
        
        cmd_sql = """
            DELETE FROM serie 
            WHERE id_serie = %s;
        """
        
        valores = (id,)
        
        try:
            db_cursor.execute(cmd_sql, valores)
            db_connection.commit()
            print("Serie removida com sucesso!")
        except Exception as e:
            print(f"Erro ao remover serie: {e}")
        finally:
            db_connection.close()
    
def teste_serie():
    
    serie_banco = SerieBanco()
    
    '''id = 1
    
    print("\nserie removido...")
    serie_banco.delete_serie(id)
    
    nome = "teen wolf"
    ano = "2011"
    classificacao = "14"
    temporadas = 9
    
    print("Inserindo nova seriee...")
    serie_banco.insert_new_serie(nome, ano, classificacao, temporadas)'''
    
    id = 3
    novo_nome = "ST"
    novo_ano = "2011"
    nova_classificacao = "16"
    nova_temporadas = "10"

    print("\nAtualizando...")
    serie_banco.update_serie(id, novo_nome, novo_ano, nova_classificacao,nova_temporadas)
    
    print("\nFilmes após a atualização:")
    series = serie_banco.get_all_series("*")
    for serie in series:
        print(f"Id: {serie.get_id()},Nome: {serie.nome} Ano: {serie.ano}, Classificação: {serie.classificacao},  Temporadas: {serie.temporada}")
