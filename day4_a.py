with open('./others/d4.txt', 'r') as f:
    nums, *boards = f.read().split('\n\n')
    f.close()

nums = list(map(int, nums.split(',')))
sp_boards = [[[int(i) for i in x.split()] for x in r.split('\n') if x] for r in boards]

def mark(board, n):
    assert len(board) == 5
    for i in range(5):
        board[i] = [x if x != n else 'X' for x in board[i]]
    return board

def left(board):
    ttl = 0
    for row in board:
        for x in row:
            if x != 'X':
                ttl += x
    return ttl

def check(nums, sp_boards):
    for n in nums:
        for i, board in enumerate(sp_boards):
            # mark
            sp_boards[i] = mark(board, n)
        # check
        for i, board in enumerate(sp_boards):
            for row in board:
                if set(row) == {'X'}:
                    return n * left(board)
            cols = [[row[i] for row in board] for i in range(5)] 
            for c in cols:
                if set(c) == {'X'}:
                    return n * left(board)

    return None

print(check(nums, sp_boards))

