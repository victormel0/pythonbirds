class Pessoa:
    def __init__(self,*filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')  #filho atribuido ao objeto andre
    andre = Pessoa(renzo, nome='Andre')
    print(Pessoa.cumprimentar(andre))
    print(id(andre))
    print(andre.cumprimentar())
    #p.nome = 'Victor'
    print(andre.nome)
    print(andre.idade)
    for filho in andre.filhos:
        print(filho.nome)
    andre.sobrenome = 'Ramalho' #criação de atributo dinamico fazendo atribuição
    del andre.filhos  #contrário dessa operação com del
    print(andre.__dict__)  #os atributos de instancia ficam presentes no atributo especial dunder dict
    print(renzo.__dict__)