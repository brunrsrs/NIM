# NIM
## Partida ~completamente justa e balanceada de NIM :)~ feita para um curso básico de programação em python

***Como funciona NIM?***

**N peças são inicialmente dispostas numa mesa ou tabuleiro**. O jogador e seu oponente jogam  **alternadamente**, retirando **pelo menos 1 e no máximo M peças** cada um. Para esse programa, os valores de N e M são escolhidas pelo usuário porém quem joga primeiro é escolhido pelo computador. **Quem tirar as últimas peças possíveis ganha o jogo**.

***Regras***

- O jogador deve escolher um N para ser o máximo de peças no tabuleiro tal que N deve ser maior que 1. Deve escolher também um M para ser o máximo de peças que podem ser removidas por jogada. M deve ser menor que N e maior que 1.
- O "computador" irá escolher então quem fará a primeira jogada.
- O jogador no seu turno deve escolher um valor para retirar tal que esse valor seja maior ou igual a 1 e menor ou igual a M
- O programa fornece a opção de partida "isolada" e de "campeonato". A diferença entre ambos é que "campeonato" são 3 "partidas isoladas" consecutivas.

**~*O macete*~**

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente. Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!". Caso contrário, o computador toma a iniciativa de começar o jogo, declarando "Computador começa!", garantindo assim que ele será vitorioso por escolher a condição que melhor lhe favorece. 
