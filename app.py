#classe composicao
#tenho duas classes e o relacionamento nao é de heranca mas tenho uma classe e que um dos atributos é atributo da outra classe
#pra uma existir precisa da outra
#uma das classes é depenente, a outra nao, so uma é dependente
#classes totalmente diferentes e pra outra existir precisa da outra, é unilateral

from modulo import *

if __name__=='__main__':
    #instacia dos objetos
    endereco_pessoal = Endereco('','','','')
    usuario = Pessoa('',0,'')

    #entrada de dados 
    usuario.nome            = input('Informe o nome do usuario: ')
    usuario.idade           = int(input('Informe a idade do usuario: '))
    endereco_pessoal.cep    = input('Informe o CPF: ')
    endereco_pessoal.uf     = input('Informe a UF: ')
    endereco_pessoal.cidade = input('Informe a cidade: ')
    endereco_pessoal.bairro = input('Informe o bairro: ')

    #composicao usuario-endereco
    usuario.endereco        = endereco_pessoal

    #saida de dados
    print(usuario.obter_info_pessoal())