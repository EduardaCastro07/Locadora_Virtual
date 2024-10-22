class Filme:
    
    def __init__(self, id_filme,nome_filme, ano_filme, classificacao_filme, username):
        self.id = id_filme
        self.nome = nome_filme
        self.ano = ano_filme
        self.classificacao = classificacao_filme
        self.username = username
        
    def __str__(self):
        return self.nome

    def get_nome(self):
        return self.nome
