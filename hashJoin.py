import hashlib

def hash_function(chave):
    func = hashlib.md5()
    func.update(chave)
    return int(func.hexdigest(),16)

def ler_tabela(txt):
    tabela = open(txt, 'r')
    linhas = tabela.readlines();
    tuplas = [tuple(x.replace('\n', '').split(';')) for x in linhas]
    tabela.close()
    return tuplas



def make_Join(tabela1, indice_atributo1, tabela2, indice_atributo2):
    particoes1 = {}
    particoes2 = {}
    tabela_join = []

    for t in tabela1:
        if t[0] == '':
            continue
        else:
         key = hash_function(t[indice_atributo1].encode('utf-8'))
         #articoes1 = {}
         if key in particoes1:
             particoes1[key].append(t)
         else:
             particoes1[key] = [t]

    for t in tabela2:
        if t[0] == '':
            continue
        else:
         key = hash_function(t[indice_atributo2].encode('utf-8'))

         if key in particoes2:
             particoes2[key].append(t)
         else:
             particoes2[key] = [t]

    for key in particoes1:
        if particoes2.get(key) == None:
         break
        else:
         for t in particoes1[key]:
             for t2 in particoes2[key]:
                 if t[indice_atributo1] == t2[indice_atributo2]:
                     tupla = t+t2
                     tabela_join.append(tupla)



    return tabela_join

gravadora = ler_tabela('gravadora.txt')
cds = ler_tabela('cd.txt')
faixas = ler_tabela('faixa.txt')

join = make_Join(gravadora, 0, cds, 2)

print('primaeira união')
for t in join:
    print(t)
print('segunda união')
final_join = make_Join(join, 3, faixas, 1)

for t in final_join:
    print(t)
