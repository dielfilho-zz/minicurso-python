# -*- encoding: UTF-8 -*-

arq = open("arquivo.txt", "w+")

lista = arq.readlines()
print lista
indice = 1  


for nome in lista:
    nome = str(indice)+" - "+nome
    indice += 1
    print nome
    arq.write(nome)
    
arq.close()
