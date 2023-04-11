import random

def desenha_forca(tentativas):
    if(tentativas == 6):
        print("-----¬\n|    |\n|    \n|    \n|  \n|\n")
    elif(tentativas == 5):
        print("-----¬\n|    |\n|    O\n|    \n|   \n|\n")
    elif(tentativas == 4):
        print("-----¬\n|    |\n|    O\n|    | \n|   \n|\n")
    elif(tentativas == 3):
        print("-----¬\n|    |\n|    O\n|   /| \n|   \n|\n")
    elif(tentativas == 2):
        print("-----¬\n|    |\n|    O\n|   /|\\ \n|   \n|\n")
    elif(tentativas == 1):
        print("-----¬\n|    |\n|    O\n|   /|\\ \n|   / \n|\n")
    elif(tentativas == 0):
        print("-----¬\n|    |\n|    O\n|   /|\\ \n|   / \\ \n|\n")

def joga():
	print("\n*******************")
	print("Jogo da forca")
	print("*******************\n")

	wordlist = []
	lista = open("games/lista_forca.txt", "r")

	for linha in lista:
		linha = linha.strip().upper()
		wordlist.append(linha)
	lista.close()	

	num = random.randrange(0, len(wordlist))	
	palavra = wordlist[num]
	palavra_secreta = ["_" for n in palavra]
	letras_chutadas = []
	tentativas = 6

	while(True):
		print(palavra_secreta)
		chute = input("\nDigite uma letra: ")
		chute = chute.strip().upper()

		if (chute in palavra):
			index = 0
			for letra in palavra:
				if(chute==letra):
					palavra_secreta[index] = chute
				index += 1
		else:
			tentativas -= 1

		letras_chutadas.append(chute)	
		letras = {n for n in letras_chutadas}
		print("\n",letras)

		desenha_forca(tentativas)

		if(tentativas==0):
			print("\n¬¬¬Perdeu!!!\n")
			print(palavra)
			break
		elif( "_" not in palavra_secreta):
			print(palavra_secreta)
			print("\n\n¬¬¬Você ganhou!!!!")
			break



if (__name__ == '__main__'):
	joga()	
