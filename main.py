import hashJoin

'''
Módulo que irá implementar o hash Join de forma definitiva.
'''


def hash(tabelas):
    nun_ref = 0

    while len(tabelas) != 1:
        print('entrou')

        aux = len(tabelas[1][0])
        print(aux)
        juncao = hashJoin.make_Join(tabelas[0], nun_ref, tabelas[1], len(tabelas[1][0]) - 1)
        tabelas.pop(0)
        tabelas.pop(0)
        tabelas.insert(0, juncao)
        nun_ref = aux

    return tabelas[0]


if __name__ == '__main__':
    gravadora = hashJoin.ler_tabela('gravadora.txt')
    cds = hashJoin.ler_tabela('cd.txt')
    faixas = hashJoin.ler_tabela('faixa.txt')

    tabelas = [gravadora, cds, faixas]
    print(tabelas)
    juncao = hash(tabelas)

    for j in juncao:
        print(j)
