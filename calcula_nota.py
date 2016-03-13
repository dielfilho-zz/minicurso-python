# -*- coding: UTF-8 -*-
# Esse script calcula a média de nota
# de um aluno e informa se o mesmo está
# aprovado, de avaliação final ou reprovado

#Pegando o nome do aluno
nome_aluno = raw_input("Digite seu nome: ")

try:
	nota1 = float(raw_input("Digite sua primeira nota: "))
	nota2 = float(raw_input("Digite sua segunda nota: "))
	nota3 = float(raw_input("Digite sua terceira nota: "))

	media = (nota1 + nota2 + nota3) / 3

	print media

	if media >= 7:
		print nome_aluno+", você está aprovado!"
	elif media >= 4:
		print nome_aluno+", você está de final!"
	else:
		print nome_aluno+", meus pêsames!"

except:
	print "Ops, ocorreu um erro!\nExecute novamente!"


