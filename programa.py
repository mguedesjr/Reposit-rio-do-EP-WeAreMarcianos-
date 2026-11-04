import funcoes
grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     

tamanho = [4,3,2,1]
quantidade = [1,2,3,4]
i = 0
for nome_navio in frota.keys():
    j = 0
    tamanho_navio = tamanho[i]
    while j < quantidade[i]:
        print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho_navio}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if tamanho_navio>1:
            orientacao = int(input("[1] Vertical [2] Horizontal >"))
            if orientacao == 1:
                orientacao = "vertical"
            elif orientacao == 2:
                orientacao = "horizontal"
        valida = funcoes.posicao_valida(frota, linha, coluna, orientacao,tamanho_navio)
        while valida == False:
            print("Esta posição não está válida!")
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho_navio}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if tamanho_navio>1:
                orientacao = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao == 1:
                     orientacao = "vertical"
                elif orientacao == 2:
                      orientacao = "horizontal"
            valida = funcoes.posicao_valida(frota, linha, coluna, orientacao,tamanho_navio)
        funcoes.define_posicoes(linha, coluna, orientacao, tamanho_navio)
        funcoes.preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho_navio)
        j+=1
    i+=1

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = funcoes.posiciona_frota(frota_oponente)
tabuleiro_jogador = funcoes.posiciona_frota(frota)
tabuleiros = funcoes.monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente)
print(tabuleiros)
jogando = True
mostra_tabuleiro = True
lista_jogadas = []
i=0
while jogando == True:
    mostra_tabuleiro = True
    linha = int(input("Jogador, qual linha deseja atacar? "))
    while (linha > 9 or linha < 0):
        print("Linha inválida!")
        linha = int(input("Jogador, qual linha deseja atacar? "))
    coluna = int(input("Jogador, qual coluna deseja atacar? "))
    while (coluna > 9 or coluna < 0):
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))
    if [linha,coluna] in lista_jogadas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
            mostra_tabuleiro = False
    else:
        lista_jogadas.append([linha,coluna])
    if i%2 == 0:
        if tabuleiro_oponente[linha][coluna] == 1:
            i += 0
        else:
            i += 0
        tabuleiro_oponente = funcoes.faz_jogada(tabuleiro_oponente,linha,coluna)
        afundados = funcoes.afundados(frota_oponente,tabuleiro_oponente)
        if afundados == 10:
            print ("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False
            mostra_tabuleiro = False
    # elif i%2 == 1:
    #     if tabuleiro_jogador[linha][coluna] == 1:
    #         i += 0
    #     else:
    #         i += 1
    #     tabuleiro_jogador = funcoes.faz_jogada(tabuleiro_jogador,linha,coluna)
    #     afundados = funcoes.afundados(frota,tabuleiro_jogador)
    #     if afundados == 10:
    #         print ("Parabéns! Você derrubou todos os navios do seu oponente!")
    #         jogando=False
    #         mostra_tabuleiro = False
    if mostra_tabuleiro == True:
        print(funcoes.monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))