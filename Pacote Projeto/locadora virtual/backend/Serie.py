class Serie:
    
    def __init__(self, id_serie,nome_serie, ano_serie, classificacao_serie,temporadas):
        self.id = id_serie
        self.nome = nome_serie
        self.ano = ano_serie
        self.classificacao = classificacao_serie
        self.temporada = temporadas       
    def __str__(self):
        return self.nome

    def get_nome(self):
        return self.nome