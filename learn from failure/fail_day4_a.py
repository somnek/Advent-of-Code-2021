# =========================================
with open('../others/d4t.txt', 'r') as f:
    ins = [line.strip() for line in f.readlines() if line.strip()]
    f.close()

width, height = 5, 5
numbers = list(map(int, ins[0].split(',')))
ins.pop(0) # remove numbers line
boards = []

for i in range(0, len(ins), width):
    board = []
    for j in range(5):
        row = [int(x) for x in ins[i+j].split()]
        board.append(row)

    boards.append(board)

def crossout(board, n):
    for row in board:
        for i in range(len(row)):
            if row[i] == n:
                row[i] = 'X'
    return board

def check_match(boards):
    # row
    for board in boards:
        for row in board:
            if row.count('X') == 5:
                return True, boards.index(board)
    # col
    for board in boards:
        for i in range(5):
            col = [board[j][i] for j in range(5)]
            if col.count('X') == 5:
                return True, boards.index(board)
    return False, None

for n in numbers:
    for i in range(len(boards)):
        marked = crossout(board, n)
        boards[i] = marked
    bingo, board_id = check_match(boards)
    if bingo:
        leftover = sum([x for row in boards[board_id] for x in row if x != 'X'])
        print(f"Bingo! stopped at {n}! left over sum: {leftover}")
        final = leftover * n
        print(final)
        break
       
