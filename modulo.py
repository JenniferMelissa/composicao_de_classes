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
    
class Telefone:
    def __init__(self, telefone_emergencial, celular, telefone_residencial):
        self.__telefone_emergencial = telefone_emergencial
        self.__celular              = celular
        self.__telefone_residencial = telefone_residencial

    @property
    def telefone_emergencial(self):
        return self.__telefone_emergencial

    @telefone_emergencial.setter
    def telefone_emergencial(self, telefone_emergencial):
        self.__telefone_emergencial = telefone_emergencial

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        self.__celular = celular

    @property
    def telefone_residencial(self):
        return self.__telefone_residencial

    @telefone_residencial.setter
    def telefone_residencial(self, telefone_residencial):
        self.__telefone_residencial = telefone_residencial

        #metodo de acao
    def obter_telefone(self):
        return f'{self.__telefone_emergencial}, {self.__celular}, {self.telefone_residencial}.'


class Pessoa:
    def __init__(self, nome, idade, endereco, telefone):
        self.__nome     = nome
        self.__idade    = idade
        self.__endereco = endereco #composicao
        self.__telefone = telefone

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

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    #metodo de acao
    def obter_info_pessoal(self):
        return f'{self.__nome}, {self.__idade} anos, mora em {self.__endereco.obter_endereco()}. Números para contato: {self.__telefone.obter_telefone()}' 
        #composicao #colocando o metodo de outra class dentro de um atributo de outra classe
