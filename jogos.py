from games import adivinhacao
from games import forca

print("\n*******************")
print("-------Jogos-------")
print("*******************\n")

while(True):
	
    escolha = int(input("Escolha seu jogo:\n1-Adivinhação \n2-Forca\n3-Sair\n"))

    if(escolha == 1):
        adivinhacao.joga()
        break
    elif(escolha == 2):
        forca.joga()
        break
    elif(escolha == 3):
        break
    else:
        print("\nOpção inválida\n")
