# -*- coding: UTF-8 -*-

#Esse código apresenta a sintáxe básica de uma 
#estrutura de repetição while

#O usuário digita o nome e a quantidade de vezes
#que esse nome será mostrado na tela.
nome = raw_input("Digite seu nome:")
vezes = int(raw_input("Digite a quantidade de vezes:"))

#Variável temporária usada apenas para 
#controlar a condição do while
temp = 0

#Enquanto temp for menor que a quantidade de vezes que o usuário quer
#que seu nome aparece, printe o nome na tela, depois incremente temp
while temp < vezes:
	print nome
	temp = temp + 1

