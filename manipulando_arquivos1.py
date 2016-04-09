# -*- encoding: UTF-8 -*-

arq = open("arquivo.txt", "r")

listaNomes = arq.readlines()

indice = 1

# Com 2 listas o gasto de memória é maior
# listaNomeArq = []

for nome in listaNomes:
    nome = str(indice)+" - "+nome
    listaNomes[indice-1] = nome
    indice = indice + 1
    
#     listaNomeArq.append(nome)
    
print listaNomes
# print listaNomeArq
    
arq.close()    

arq = open("arquivo.txt", "w")

for nome in listaNomes:
    arq.write(nome)

arq.close()
    
    
    
    
    
    
    
    
    
    