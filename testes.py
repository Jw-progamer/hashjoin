'''Implementação prática do código de Hash Join.

As tabelas estão armazenadas em arquivos txt.
para todos os efeitos, estamos considerando a seguinte consulta:
select * from gravadora inner join cd inner join faixa on cod_cd = cod_cd on cod_gravadora = cod_gravadora
'''

import hashlib as hash

'''Primeiro, carregar a tabela cd na memória'''
tabelaGravadora = open('gravadora.txt','r')
linhasGravadora = tabelaGravadora.readlines();
tuplasGravadora = [tuple(x.replace('\n','').split(';')) for x in linhasGravadora]
tabelaGravadora.close()

print(tuplasGravadora)

'''Agora definir partições para as tuplas'''

for t in tuplasGravadora:
    bucketNumber = hash.md5()
    bucketNumber.update(t[0].encode('utf-8'))
    print(int(bucketNumber.hexdigest(),16))

tabelaCds = open('cd.txt','r')
linhasCds = tabelaCds.readlines();
tuplasCds = [tuple(x.replace('\n','').split(';')) for x in linhasCds]

print(tuplasCds)

for t in tuplasCds:
    bucketNumber = hash.md5()
    bucketNumber.update(t[2].encode('utf-8'))
    print(int(bucketNumber.hexdigest(),16))