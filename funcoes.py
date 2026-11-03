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