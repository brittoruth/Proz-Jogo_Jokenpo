import random
import time

print("\n--------- Bem vindo ao Jokenpô --------- \n!!!(じゃんけんぽん いらっしゃいませ)!!!")
#print() >>> explicar as regras básicas (um resumo do arquivo de regras do jogo)


scoreJogador = 0
scoreBot = 0

while scoreJogador <3 or scoreBot <3:
  
    configuracaoMao = {
        0 : "Pedra",
        1 : "Papel",
        2 : "Tesoura" 
    }

    botRandom = random.randint(0,2)
    escolhaJogador = int(input("\nInforme sua configuração de mão: \n[0] Pedra \n[1] Papel \n[2] Tesoura \n>>> "))
       
    time.sleep(1)
    print("Jan")
    time.sleep(1)
    print("Ken")
    time.sleep(1)
    print("Pô!\n")
    print("Você jogou: "+ configuracaoMao[escolhaJogador])
    print("Seu oponente jogou "+ configuracaoMao[botRandom])

    if escolhaJogador == botRandom: # se impatou repete round (mesma configuração)
        print("Empate. Vamos de novo!\n")

    elif escolhaJogador == 0 and botRandom == 1:
        print("Você perdeu a mão :()")
        scoreBot += 1
        print(f"Seu saldo de vitórias: {scoreJogador} \nSaldo de vitórias do seu adversário: {scoreBot}")
    elif escolhaJogador == 0 and botRandom == 2: 
        print("Você ganhou a mão :)")
        scoreJogador += 1
        print(f"Seu saldo de vitórias: {scoreJogador} \nSaldo de vitórias do seu adversário: {scoreBot}")

    elif escolhaJogador == 1 and botRandom == 2:
        print("Você perdeu a mão :(")
        scoreBot += 1
        print(f"Seu saldo de vitórias: {scoreJogador} \nSaldo de vitórias do seu adversário: {scoreBot}")
    elif escolhaJogador == 1 and botRandom == 0: 
        print("Você ganhou a mão :)")
        scoreJogador += 1
        print(f"Seu saldo de vitórias: {scoreJogador} \nSaldo de vitórias do seu adversário: {scoreBot}")

    elif escolhaJogador == 2 and botRandom == 0:
        print("Você perdeu a mão")
        scoreBot += 1
        print(f"Seu saldo de vitórias: {scoreJogador} \nSaldo de vitórias do seu adversário: {scoreBot}")
    elif escolhaJogador == 2 and botRandom == 1: 
        print("Você ganhou a mão")
        scoreJogador += 1
        print(f"Seu saldo de vitórias: {scoreJogador} \nSaldo de vitórias do seu adversário: {scoreBot}")
    
    if scoreBot == 3:
        print("Você perdeu o jogo! \nTente outra vez!")
        break
    if scoreJogador == 3:
        print("\nP-A-R-A-B-É-N-S!!!\nVocê GANHOU o jogo!!!! \nTente outra vez! Quem sabe nessa eu ganho de você ;)\n")
        break

# Próximo MVP(2): *Este jogo possui uma única regra: não é permitido mostrar pedra duas vezes seguidas*
# Próximo MVP(3): Adicionar tratamento de erros e exceções