class Usuario:
        
    def __init__(self, username_b=None, senha_b=None):
        self.username = username_b
        self.senha = senha_b
        
    def set_username(self, username):
        self.username = username
        
    def get_username(self):
        return self.username
        
    def get_senha(self):
        return self.senha