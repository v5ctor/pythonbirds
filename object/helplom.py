class Pessoa:
    def __init__(self,nome=None,idade=None):
        self.nome=nome
        self.idade=idade

    def digaoi(self):
        return f'Oi,{id(self)}'
if __name__ == '__main__':
    p = Pessoa('Reinaldo',34)
    print(p.nome,p.idade)
    print(Pessoa.digaoi(p))
    print(p.digaoi())
    p.nome='Víctor'
    p.idade=19
    print(p.nome)
    print(p.idade)
    print(id(p))