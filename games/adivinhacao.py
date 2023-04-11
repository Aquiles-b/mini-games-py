import random 

def joga():
	print("\n*******************")
	print("Jogo da adivinhação")
	print("*******************\n")

	print("Escolha o nível de dificuldade:")

	pontos = 1000
	range_poss = 10

	while(True):
		dif = input("1- Fácil \n2- Médio \n3- Difícil\n")

		if (dif == "1"):
			break
		elif(dif == "2"):
			range_poss = 50
			pontos = 1200
			break
		elif(dif == "3"):
			range_poss = 100
			pontos = 1300
			break
		else:
			print("Opção inválida!")

	numero_secreto = random.randrange(1,range_poss + 1)
	chances = 5

	for tentativas in range(1, chances + 1):

		print(f"Tentativa {tentativas} de {chances} \n")
		chute = input(f"Digite o seu número entre 1 e {range_poss}: ")
		
		if(chute.isnumeric()):
			chute = int(chute)
		else:
			print("\ninválido\n")
			continue
		if (chute < 1) or (chute > range_poss):
			print(f"O número está entre 1 e {range_poss}.")
			continue
		elif (numero_secreto == chute):
			print("\n**Você acertou!")
			print(f"Pontuação: {pontos}")
			break
		elif (tentativas==chances):
			print("\n Errou! \n")
			print(f"O número era {numero_secreto}.")
			break
		elif(chute > numero_secreto):
			print("\n¬¬Errou! O número é menor. \n")
		else:
			print("\n¬¬Errou! O número é maior. \n")

		pontos = pontos - abs(numero_secreto - chute)


if(__name__=="__main__"):
	joga()




