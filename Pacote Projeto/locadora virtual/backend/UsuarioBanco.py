import psycopg2
from backend.Usuario import Usuario

class UsuarioBanco:
    def __init__(self):
        pass
    
    def get_usuario_by_username(self, username):
            
        db_conn = psycopg2.connect(dbname='locadora',
                                         user="postgres",
                                         password="eduar26",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_conn.cursor()
        cmd_sql = "SELECT * FROM usuario WHERE username = %s;"
        db_cursor.execute(cmd_sql, (username,))

        linhas_banco_dados = db_cursor.fetchone()
        db_conn.commit()
        db_conn.close()
        
        if linhas_banco_dados is not None:
            username_usuario = linhas_banco_dados[0]
            senha_usuario = linhas_banco_dados[1]
                
            usuario = Usuario(username_usuario,senha_usuario)
        else:
            usuario = None

        return usuario
    
def teste():    
    usuario_banco = UsuarioBanco()
    username = "joaosilva"  
    usuario = usuario_banco.get_usuario_by_username(username)

    if usuario:
        print(f"Usuário encontrado: {usuario.username}, Senha: {usuario.senha}")
    else:
        print("Nenhum usuário encontrado com essa senha.")
