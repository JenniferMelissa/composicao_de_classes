# baixa a extensao Python getter setter 
#seleciona os atributos
#ctrl + Shift + P
#agora faça as alteracoes para se adequar ao seu codigo
class Endereco:
    def __init__(self, cep, uf, cidade, bairro):
        self.__cep    = cep
        self.__uf     = uf
        self.__cidade = cidade 
        self.__bairro = bairro

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    #metodo de acao
    def obter_endereco(self):
        return f'{self.__bairro}, {self.__cidade}, {self.__uf}, CEP: {self.__cep}.'
    
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.__nome     = nome
        self.__idade    = idade
        self.__endereco = endereco #composicao

    #metodo de acesso
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    #metodo de acao
    def obter_info_pessoal(self):
        return f'{self.__nome}, {self.__idade} anos, mora em {self.__endereco.obter_endereco()}.' 
        #composicao #colocando o metodo de outra class dentro de um atributo de outra classe
