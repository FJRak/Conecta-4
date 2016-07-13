import games

def h1(state, player):
    horizontales = 0
    verticales = 0
    diagonales = 0

    if not state.utility == 0:
        if player == 'X':
            return state.utility * 10000
        else:
            return -state.utility * 9000
    for x in range(1, 8):
        for y in range(1, 7):
            if ((x,y)) in games.ConnectFour().legal_moves(state):
                equis = x
                ygriega = y
                horizontales = horizontales + chorizontales(state, player, equis, ygriega)
                verticales = verticales + cverticales(state,player,equis,ygriega)
                diagonales = diagonales + cdiagonales(state,player,equis,ygriega)

    return horizontales + verticales + diagonales

def chorizontales (state, player, equis, ygriega):
    suma = 0
    vectores = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
    for z in range(0,4):
        if equis in vectores[z]:
            suma = suma + valor(state, player, equis, ygriega, vectores[z])

    return suma


def valor(state,player,equis,ygriega, vector):
    count = 0;
    rcount = 0;
    for x in range(0,4):
        if equis == vector[x]:
            if player == 'X':
                count = count + 10
                rcount = 0
            else:
                count = 0
                rcount = rcount + 10
            continue
        if state.board.get((vector[x], ygriega)) == 'X':
            count = count + 10
            rcount = 0
        if state.board.get((vector[x], ygriega)) == '.':
            count = count + 1
            rcount = rcount + 1
        if state.board.get((vector[x], ygriega)) == 'O':
            count = 0
            rcount = rcount + 10
            ##if (count == 0 or rcount == 0) and x >= 6:
            ##return 0
    if player == 'O':
        return rcount - count
    return count - rcount

def cverticales(state,player,equis,ygriega):
    count = 0
    rcount = 0
    for y in range(1,7):
        if ygriega == y:
            if player == 'X':
                count = count + 10
                rcount = 0
            else:
                count = 0
                rcount = rcount + 10
            continue
        if state.board.get((equis,y))=='X':
            count = count +10
            rcount = 0
        if state.board.get((equis,y))=='.':
            count = count + 1
            rcount = rcount + 1
        if state.board.get((equis,y))=='O':
            count = 0
            rcount = rcount + 10
        ##if (count ==0 or rcount ==0) and y > 4:
         ##   return 0
    if player == 'O':
        return rcount-count
    return count - rcount

def cdiagonales (state, player, equis, ygriega):
    x = equis
    y = ygriega
    seguidas = 1
    rseguidas = 1
    count = 0
    rcount = 0

    x= equis-5
    y = ygriega-5
    while x < 8 and y < 7:
        if x <1 or y<1:
            x = x + 1
            y = y + 1
            continue
        if state.board.get(x, y) == 'X':
            seguidas = seguidas + 1
            rseguidas = 0
            count = count + 10
            rcount = 0
        if state.board.get(x, y) == 'O':
            seguidas = 0
            rseguidas = rseguidas + 1
            count = 0
            rcount = rcount + 10
        if state.board.get(x, y) == '.':
            count = count + 1
            rcount = rcount + 1
        x = x + 1
        y = y + 1

    seguidas = 1
    rseguidas = 1
    x = equis + 5
    y = ygriega - 5
    while x > 0 and y < 7:
        if x == equis and y == ygriega:
            if player == 'X':
                seguidas = seguidas + 1
                rseguidas = 0
            elif player == 'O':
                rseguidas = rseguidas + 1
                seguidas = 0
        if x > 7 or y < 1:
            x = x + 1
            y = y + 1
            continue
        if state.board.get(x, y) == 'X':
            seguidas = seguidas + 1
            rseguidas = 0
            count = count + 10
            rcount = 0
        if state.board.get(x, y) == 'O':
            seguidas = 0
            rseguidas = rseguidas + 1
            count = 0
            rcount = rcount + 10
        if state.board.get(x, y) == '.':
            count = count + 1
            rcount = rcount + 1
        x = x - 1
        y = y + 1

    if player == 'O':
        if rseguidas ==3:
            rseguidas = rseguidas + 100
        return (rcount - count)+ rseguidas
    if seguidas ==3:
        seguidas = seguidas + 100
    return (count - rcount) + seguidas






def h0(state, player):
    if not state.utility==0:
        if player == 'X':
            return state.utility * 1000
        else:
            return -state.utility*1000
    max_adyacentes = 0
    min_adyacentes = 1000
    espacios = 1000

    for x in range (1,8):
        for y in range(1,7):

            if ((x,y)) in games.ConnectFour().legal_moves(state):
                equis = x
                ygriega = y
                adyacente = adyacentes(equis, ygriega, state, player)
                adyacenter = adyacentesr(equis,ygriega,state, player)
                blancos = enblanco(equis, ygriega, state )

                if adyacente > max_adyacentes:
                    max_adyacentes=adyacente

                if  adyacenter < min_adyacentes:
                    min_adyacentes = adyacenter


                if blancos < espacios:
                    espacios = blancos


    ##print max_adyacentes
    return max_adyacentes*0.8+ (8-min_adyacentes)*0.2



def adyacentes(equis, ygriega, state, player):

    count = 0
    for x in range (equis-1,equis+2):

        if x<1 or x >7:
            continue

        for y in range(ygriega-1,ygriega+2):
            if y<1 or y >6:
                continue

            if state.board.get((x,y))== player:
                count= count+1


    return count

def adyacentesr(equis, ygriega, state, player):

    count = 0
    for x in range (equis-1,equis+2):
        if x<1 or x >7:
            continue

        for y in range(ygriega-1,ygriega+2):

            if y<1 or y >6:
                continue


            if(player == 'X'):
                if state.board.get((x,y))=='O':
                    count= count+1
            else:
                if state.board.get((x,y))=='X':
                    count= count+1

    return count

def enblanco (equis, ygriega, state):
    count = 0
    for y in range (ygriega, 7):

        if state.board.get((equis,y))=='.':
            count = count +1

    return count

