import psycopg2
from backend.FilmesInfantis import Filmes_Infantis

class FilmeInfantilBanco:

    def get_filmes_infantis(self, atributo):
       
        db_connection = psycopg2.connect(dbname='locadora',
                                         user="postgres",
                                         password="eduar26",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()
        
        
        cmd_sql = f"SELECT {atributo} FROM filme WHERE classificacao_filme <= '10' OR classificacao_filme = 'livre';"
        print(cmd_sql)
        
        db_cursor.execute(cmd_sql)
        lista_filmes_infantis = db_cursor.fetchall()
        db_connection.commit()
        db_connection.close()
        
        lista_filme_resposta = []


        for filme_infantil in lista_filmes_infantis:
                
            id = filme_infantil[0]
            nome   = filme_infantil[1]
            ano  = filme_infantil[2]
            classificacao   = filme_infantil[3]
            username = filme_infantil[4]

            filme_item = Filmes_Infantis(id,nome, ano, classificacao, username)
            lista_filme_resposta.append(filme_item)
                
        return lista_filme_resposta
    
def teste_infantil():
    
    filme_infantil = FilmeInfantilBanco()
    
    print("\n todos os filmes infantis")
    filmes = filme_infantil.get_filmes_infantis("*")
    for filme in filmes:
        print(f"Id: {filme.id}, Nome: {filme.get_nome()}, Ano: {filme.ano}, Classificação: {filme.classificacao}, Senha: {filme.username}")
