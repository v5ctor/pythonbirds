class Pessoa:
    dedos_mao = 10
    def __init__(self,*filhos,nome=None,idade=None):
        self.nome=nome
        self.idade=idade
        self.filhos=list(filhos)

    def digaoi(self):
        return f'Oi,{id(self)}'
if __name__ == '__main__':
    jorge =Pessoa(nome='Jorge',idade=4)
    lucio = Pessoa(nome='Lúcio',idade=8)
    reinaldo = Pessoa(lucio,jorge,nome='Reinaldo',idade= 34)
    print(reinaldo.nome, reinaldo.idade)
    print(Pessoa.digaoi(reinaldo))
    print(reinaldo.digaoi())
    print(reinaldo.idade)
    print(id(reinaldo))
    for filho in reinaldo.filhos:
        print(filho.nome,filho.idade)
    reinaldo.sobrenome='Castro'
    lucio.sobrenome='Castro'
    del reinaldo.sobrenome
    del lucio.sobrenome
    del lucio.filhos
    del jorge.filhos
    del reinaldo.filhos
    reinaldo.dedos_mao = 9
    lucio.dedos_mao = 11
    jorge.dedos_mao = Pessoa.dedos_mao
    print(reinaldo.__dict__)
    print(lucio.__dict__)
    print(jorge.__dict__)
    print(reinaldo.dedos_mao)
    print(lucio.dedos_mao)
    print(jorge.dedos_mao)
