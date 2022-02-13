matrix = [
    ['-', '-', '-'], 
    ['-', '-', '-'], 
    ['-', '-', '-']
]

def check_coordinates(data):
    a =list(map(int, data.split()))
    if len(a) >= 2 and 0 <= a[0] <= 2 and 0 <= a[1] <= 2:
        if matrix[a[0]][a[1]] == '-':
            return a[0], a[1]
    return None

def check_winner(a):
    if matrix[0][0] == matrix[0][1] == matrix[0][2] == a \
        or matrix[1][0] == matrix[1][1] == matrix[1][2] == a \
        or matrix[2][0] == matrix[2][1] == matrix[2][2] == a \
        or matrix[0][0] == matrix[1][0] == matrix[2][0] == a \
        or matrix[0][1] == matrix[1][1] == matrix[2][1] == a \
        or matrix[0][2] == matrix[1][2] == matrix[2][2] == a \
        or matrix[0][0] == matrix[1][1] == matrix[2][2] == a \
        or matrix[0][2] == matrix[1][1] == matrix[2][0] == a:
            return True
    return False

curr_player = 1

while True:
    coords = check_coordinates(input(f'{curr_player} игрок, введите номер строки (0-2), номер столбца(0-2) '))
    if coords == None:
        print('Неправильные данные. Введите заново.')
        continue

    matrix[coords[0]][coords[1]] = 'X' if curr_player == 1 else 'O'
    print('  0 1 2')
    for i in range(3):
        print(i, *matrix[i])
    if check_winner('X' if curr_player == 1 else 'O'):
        print(f'Победил {curr_player} игрок')
        break
    if curr_player == 1:
        curr_player = 2
    else:
        curr_player = 1

        
        


        

    
    
    
