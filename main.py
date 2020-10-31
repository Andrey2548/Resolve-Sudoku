
mesa = [[4,0,0,0,5,0,8,0,0],
    [0,1,8,0,0,0,7,0,0],
    [0,0,3,0,0,4,0,0,0],
    [9,6,0,0,0,0,0,0,0],
    [0,0,5,0,0,3,0,0,0],
    [0,7,0,0,0,8,0,6,0],
    [0,0,1,6,0,0,0,0,4],
    [0,0,0,5,0,0,0,1,3],
    [0,0,0,8,0,0,0,0,0],]

def resolveSudoku(mesa):
    vazio = achaVazio(mesa)
    if not vazio:
        return True
    else:
        linha, coluna = vazio
    for i in range(1,10):
        if validaNumero(mesa, i, linha, coluna):
            mesa[linha][coluna] = i

            if resolveSudoku(mesa):
                return True
            mesa[linha][coluna] = 0
    return False

def achaVazio(mesa):
    for i in range(len(mesa)):
        for j in range(len(mesa[0])):
            if mesa[i][j] == 0:
                return (i,j)
def validaNumero(mesa, numero, linha, coluna):
    #Verifica Linha
    for i in range(len(mesa[0])):
        if mesa[linha][i] == numero and coluna !=i:
            return False
    #Verifica Coluna
    for i in range(len(mesa)):
        if mesa[i][coluna] == numero and linha !=i:
            return False
    #Verifica Matriz
    caixa_x = coluna // 3
    caixa_y = linha // 3

    for i in range(caixa_y*3, caixa_y*3 +3):
        for j in range(caixa_x*3, caixa_x*3 +3):
            if mesa[i][j] == numero and i != linha and j != coluna:
                return False
    return True
def print_board(mesa):
    for i in range(len(mesa)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(mesa[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(mesa[i][j])
            else:
                print(str(mesa[i][j]) + " ", end="")


resolveSudoku(mesa)
print_board(mesa)
