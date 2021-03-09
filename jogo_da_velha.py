#by: TioToninho
#Jogo da velha

theBoard = {'ce': '-','cm': '-','cd': '-','me': '-','mm': '-','md': '-','be': '-','bm': '-','bd': '-'}
def look():
    print(theBoard['ce'] + ' ___ ' + theBoard['cm'] + ' ___ ' + theBoard['cd'])
    print(theBoard['me'] + ' ___ ' + theBoard['mm'] + ' ___ ' + theBoard['md'])
    print(theBoard['be'] + ' ___ ' + theBoard['bm'] + ' ___ ' + theBoard['bd'])

def x_turn():
    print('Jogada do: X')
    move = input()
    theBoard[move] = 'X'
    look()
    x_win()
    x_fix()
    o_turn()

def o_turn():
    print('Jogada do: O')
    move = input()
    theBoard[move] = 'O'
    look()
    o_win()
    o_fix()
    x_turn()

def x_win():
    if theBoard['ce'] == 'X':
        if theBoard['cm'] == 'X':
            if theBoard['cd'] == 'X':
                print('X venceu!')
                input()
        elif theBoard['me'] == 'X':
            if theBoard['be'] == 'X':
                print('X venceu!')
                input()
        elif theBoard['mm'] == 'X':
            if theBoard['bd'] == 'X':
                print('X venceu!')
                input()
    elif theBoard['be'] == 'X':
        if theBoard['bm'] == 'X':
            if theBoard['bd'] == 'X':
                print('X venceu!')
                input()
    elif theBoard['cd'] == 'X':
        if theBoard['md'] == 'X':
            if theBoard['bd'] == 'X':
                print('X venceu!')
                input()
        elif theBoard['mm'] == 'O':
            if theBoard['be'] == 'O':
                print('O venceu!')
                input()

def o_win():
    if theBoard['ce'] == 'O':
        if theBoard['cm'] == 'O':
            if theBoard['cd'] == 'O':
                print('O venceu!')
                input()
        elif theBoard['me'] == 'O':
            if theBoard['be'] == 'O':
                print('O venceu!')
                input()
        elif theBoard['mm'] == 'O':
            if theBoard['bd'] == 'O':
                print('O venceu!')
                input()
    elif theBoard['be'] == 'O':
        if theBoard['bm'] == 'O':
            if theBoard['bd'] == 'O':
                print('O venceu!')
                input()
    elif theBoard['cd'] == 'O':
        if theBoard['md'] == 'O':
            if theBoard['bd'] == 'O':
                print('O venceu!')
                input()

def o_fix():
    if theBoard['cd'] == 'O':
        if theBoard['mm'] == 'O':
            if theBoard['be'] == 'O':
                print('O venceu!')
                input()
    if theBoard['cm'] == 'O':
        if theBoard['mm'] == 'O':
            if theBoard['bm'] == 'O':
                print('O venceu!')
                input()

def x_fix():
    if theBoard['cd'] == 'X':
        if theBoard['mm'] == 'X':
            if theBoard['be'] == 'X':
                print('X venceu!')
                input()
    if theBoard['cm'] == 'X':
        if theBoard['mm'] == 'X':
            if theBoard['bm'] == 'X':
                print('X venceu!')
                input()

look()
x_turn()
