def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('| ' + ' | '.join(linha) + ' |')
    print()


def movimento_valido(tabuleiro, linha, coluna):
    return (
        0 <= linha < len(tabuleiro) and
        0 <= coluna < len(tabuleiro[0]) and
        tabuleiro[linha][coluna] == ' '
    )


def chegou_destino(linha, coluna):
    return linha == 0 and coluna == 3


def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    melhor_profundidade = float('inf')
    melhor_linha = linha_atual
    melhor_coluna = coluna_atual

    direcoes = [
        (0, 1),   # Direita
        (0, -1),  # Esquerda
        (-1, 0),  # Cima
        (1, 0)    # Baixo
    ]

    for dx, dy in direcoes:
        nova_linha = linha_atual + dx
        nova_coluna = coluna_atual + dy

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            if chegou_destino(nova_linha, nova_coluna):
                return nova_linha, nova_coluna, profundidade

            
            tabuleiro[nova_linha][nova_coluna] = '*'

            
            linha_final, coluna_final, nova_profundidade = proximo_movimento(
                tabuleiro, nova_linha, nova_coluna, profundidade + 1
            )

            
            tabuleiro[nova_linha][nova_coluna] = ' '

            if nova_profundidade < melhor_profundidade:
                melhor_profundidade = nova_profundidade
                melhor_linha = linha_final
                melhor_coluna = coluna_final

    return melhor_linha, melhor_coluna, melhor_profundidade


def main():
    
    tabuleiro = [
        [' ', ' ', 'X', ' ', ' '],
        ['X', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', 'X', 'X', ' ', 'X']
    ]

    linha_atual = 2
    coluna_atual = 1
    
    tabuleiro[linha_atual][coluna_atual] = '*'

    mostrar_tabuleiro(tabuleiro)

    while not chegou_destino(linha_atual, coluna_atual):
        nova_linha, nova_coluna, profundidade = proximo_movimento(
            tabuleiro, linha_atual, coluna_atual, 1
        )

        if profundidade == float('inf'):
            print("Caminho impossível!")
            return

        linha_atual = nova_linha
        coluna_atual = nova_coluna
        tabuleiro[linha_atual][coluna_atual] = '*'

        mostrar_tabuleiro(tabuleiro)

    print("Chegamos ao destino! 🏁")


main()