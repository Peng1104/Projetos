import re

print("CALCULADOR DE CORRNETES")
print()
print("Quantas Resistências?")

Numero_de_Resistências = input("Numero de Resistências: ")
print()

i = 0

if not re.search("^\d+$", Numero_de_Resistências):
	print("#########################################################")
	print("               ERRO: Escreva um número                   ")
	print("#########################################################")
	print()
else:
	Quantidade_de_Resistências = int(Numero_de_Resistências)
	Resistências = []

	while(len(Resistências) != Quantidade_de_Resistências):
		Rx = input("R{0} = ".format(len(Resistências)+1))
		print()

		i = 0

		teste = Rx

		while i < Quantidade_de_Resistências:
			teste = teste.replace("R{0}".format(i), "0")
			i = i + 1

		try:
			eval(teste)

		except:
			print("#########################################################")
			print("       ERRO: Escreva um número ou equação valida         ")
			print("#########################################################")
			print()
			continue

		Resistências.append(Rx)

	print("Os valores das Resistências são:")
	print()

	i = 0

	for R in Resistências:
		print("R{0} = {1}".format(i, R))
		i = i + 1

	print()
	print("Quantas Equações?")
	Numero_de_Equações = input("Numero de Equações: ")

	if re.search("^\d+$", Numero_de_Equações):

		Equações = []
		Matriz = []
		Vetor = []

		while len(Vetor) != int(Numero_de_Equações):
			print("Escreva a {0}° Equação:".format(len(Vetor)+1))
			Equação = input("> ")
			print()

			if len(Equação).split("=") == 2:
				Valor = Equação.split("=")[0]
				Resultado = Equação.split("=")[1]

				i = 0

				for R in Resistências:
					Resultado.replace("R{0}".format(i), str(R))
					i = i + 1

				try:
					Resultado_Final = float(eval(Resultado))
				except:
					print("#########################################################")
					print("                ERRO: Equação Invalida                   ")
					print("#########################################################")
					print()
					continue


				"""
				Construir a linha da matriz de maneira mais correta
				"""

				i = 0

				for R in Resistências:
					Valor.replace("R{0}".format(i), str(R))
					i = i + 1

				Linha = []

				for x in Valor.split(" "):
					try:
						Linha.append(eval(x))
					except:
						print("#########################################################")
						print("                ERRO: Equação Invalida                   ")
						print("#########################################################")
						print()
						continue

				if len(Linha) != Quantidade_de_Resistências:
					print("#########################################################")
					print("                ERRO: Equação Invalida                   ")
					print("#########################################################")
					print()
					continue

				Resultado_Final = 0

				Matriz.append(Linha)
				Vetor.append(Resultado_Final)
				Equações.append(Equação)

		print("Suas Equações")

		print("Sua Matriz é:")
		print()

		for Linha in Lista_de_Equações:
			print(Linha)

		print()
		
		if input("Tudo Certo? [S|N] \nResposta: ").lower() == "s":
			Tensões = []

			while len(Tensões) != int(Numero_de_Equações):
				print("Qual o valor da {0}° Tensão?".format(len(Tensão)+1))
				Tensão = input("> ")
				print()

				if re.search("^\d+(.\d+)?$", Tensão):
					Tensões.append(float(Tensão))
				else:
					print()
	else:
		print("#########################################################")
		print("               ERRO: Escreva um número                   ")
		print("#########################################################")
		print()

print()
print("Programa Finaizado!")