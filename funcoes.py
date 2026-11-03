def define_posicoes (linha, coluna, orientacao, tamanho):
    lista = []
    if orientacao == "vertical":
        i = 0
        while i < tamanho:
            lista.append([linha+i,coluna])
            i+=1
    elif orientacao == "horizontal":
        i = 0
        while i < tamanho:
            lista.append([linha,coluna+i])
            i+=1
    return lista

def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio not in frota.keys():
        frota[nome_navio] = []
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    else:
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:   
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    i = 0
    while i < 10:
        tabuleiro.append([0]*10)
        i+=1
    for nome_navio in frota:
        for posicoes in frota[nome_navio]:
            for posicao in posicoes:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro