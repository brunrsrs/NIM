
def computador_escolhe_jogada(n, m):
    retirar = m
    while (retirar>=1 and ((n-retirar)%(m+1))!=0 ):
        retirar-=1

    if (retirar<1):
        retirar = m
    
    n = n-retirar
    if (retirar>1):
        print("\nO computador tirou", retirar, "peças.")
    else: 
        print("\nO computador tirou uma peça.")

    return retirar

def usuario_escolhe_jogada(n, m):
    retirar = 0
    while (retirar < 1 or retirar > m or retirar > n):
        retirar = int(input("\nQuantas peças você vai tirar? "))
        if (retirar < 1 or retirar > m):
            print("\nOops! Jogada inválida! Tente de novo.")
        else:
            n = n-retirar
            if (retirar>1):
                print("\nVoce tirou", retirar, "peças.")
            else: 
                print("\nVocê tirou uma peça.")
            return retirar

def partida():
    vencedor=0
    n = 0
    while (n <= 1):
        n = int(input("Quantas peças? "))
        if (n <= 1):
            print("Número Inválido")
    m = n
    while (m >= n or m < 1):
        m = int(input("Limite de peças por jogada? "))
        if (m >= n or m < 1):
            print("Número Inválido")

    if ((n%(m+1))==0):
        print("\nVoce começa!")
        aux = usuario_escolhe_jogada(n, m)
        n = n-aux
        if (n>1):
            print("Agora restam", n, "peças no tabuleiro.")
        else:
            print("Agora resta apenas uma peça no tabuleiro.")

    else:
        print("\nComputador começa!")
    
    while(n>0):
        aux = computador_escolhe_jogada(n, m)
        n = n-aux
        if ( n > 1):
            print("Agora restam", n, "peças no tabuleiro.")
        elif (n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            vencedor = 0
            break

        aux = usuario_escolhe_jogada(n, m)
        n = n-aux
        if (n>1):
            print("Agora restam ", n, " peças no tabuleiro.")
        elif (n==1):
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            vencedor = 1
            break
    
    return vencedor


def main():
    opt = 0
    while (opt != 1 and opt != 2):
        opt = int(input("\nBem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\nEscolha: "))

    if (opt == 1):
        print("Voce escolheu uma partida isolada!")
        venceu = partida()
        if (venceu == 0):
            print("Fim do jogo! O computador ganhou!")
        else:
            print("Fim do jogo! O usuário ganhou!")

    elif(opt == 2):
        p_computador = 0
        p_usuario = 0
        print("Voce escolheu um campeonato!")
        for i in range(3):
            print("\n**** Rodada", i+1, "****\n")
            venceu = partida()
            if (venceu == 0):
                print("Fim do jogo! O computador ganhou!")
                p_computador+=1
            else:
                print("Fim do jogo! O usuário ganhou!")
                p_usuario+=1

        print("\n**** Final do campeonato! ****\n")
        print("Placar: Você", p_usuario, "X", p_computador, "Computador")

    else:
        print("Valor inválido")

main()
