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
print(frota)



