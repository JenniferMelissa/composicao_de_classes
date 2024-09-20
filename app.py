#classe composicao
#tenho duas classes e o relacionamento nao é de heranca mas tenho uma classe e que um dos atributos é atributo da outra classe
#pra uma existir precisa da outra
#uma das classes é depenente, a outra nao, so uma é dependente
#classes totalmente diferentes e pra outra existir precisa da outra, é unilateral

from modulo import *

if __name__=='__main__':
    #instacia dos objetos
    endereco_pessoal = Endereco('','','','')
    usuario = Pessoa('',0,'','')
    telefone = Telefone('','','')

    #entrada de dados usuario
    usuario.nome            = input('Informe o nome dso usuario: ')
    usuario.idade           = int(input('Informe a idade do usuario: '))

    #composicao usuario-endereco
    usuario.endereco        = endereco_pessoal

    #entrada de dados endereco
    endereco_pessoal.cep    = input('Informe o CPF: ')
    endereco_pessoal.uf     = input('Informe a UF: ')
    endereco_pessoal.cidade = input('Informe a cidade: ')
    endereco_pessoal.bairro = input('Informe o bairro: ')

    usuario.telefone = telefone

    telefone.telefone_emergencial = input('Informe um telefone emergencial: ')
    telefone.celular = input('Informe um número de celular: ')
    telefone.telefone_residencial = input('informe um telefone residencial: ')

    #saida de dados
    print(usuario.obter_info_pessoal())