"""" RASCUNHO DAS REGRAS (PRA FACILITAR A CODAGEM, DEPOIS EXCLUIMOS NO FINAL ;) )
- Pedra ganha da tesoura (amassando-a ou quebrando-a).
- Tesoura ganha do papel (cortando-o).
- Papel ganha da pedra (embrulhando-a).

A pedra é simbolizada por um punho fechado; 
a tesoura, por dois dedos esticados; 
e o papel, pela mão aberta. 
Caso dois jogadores façam o mesmo gesto, ocorre um empate, 
e geralmente se joga de novo até desempatar. 
*Este jogo possui uma única regra: não é permitido mostrar pedra duas vezes seguidas*.
"""

import random
import time

print("--------- Bem vindo ao Jokenpô --------- \n!!!(じゃんけんぽん いらっしゃいませ)!!!")
#print() >>> explicar as regras básicas (um resumo do arquivo de regras do jogo)

scoreJogador = 0
scoreBot = 0
partidaFinalizada = False

while partidaFinalizada == False:
    configuracaoMao = ["Pedra", "Papel", "Tesoura"]
    jogadorBot = random.choice(configuracaoMao)
    escolhaJogador = int(input("Informe sua configuração de mão: \n[0] Pedra \n[1] Papel \n[2] Tesoura \n>>>"))
       
    time.sleep(1)
    print("Jan")
    time.sleep(1)
    print("Ken")
    time.sleep(1)
    print("Pô!\n")
    print("Você jogou: "+ configuracaoMao[escolhaJogador])
    print("Seu oponente jogou "+ jogadorBot)
    if jogadorBot == configuracaoMao[escolhaJogador]: # se impatou repete round (mesma configuração)
        print("Empate. Vamos de novo!")
    
#Daqui pra baixo tá em contrução - parte de cima tá 100% funcionando
          
          #Quem ganho a mão Acrua +1
        # precisa construir as condicionais
    if escolhaJogador == 0 and jogadorBot == 2:
        scoreJogador = + 1
        
    if escolhaJogador == 0 and jogadorBot == 1:
        scoreBot = + 1
    
    if escolhaJogador == 1 and jogadorBot == 0:
        scoreJogador = + 1

    if escolhaJogador == 1 and jogadorBot == 2:
        scoreBot = + 1

# se input atual máquina ou jogador  == input máquina ou jogador anterior não permitir jogada
# *Este jogo possui uma única regra: não é permitido mostrar pedra duas vezes seguidas*



# repetir jogo até vitorioso +3 placar
