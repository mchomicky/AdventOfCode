import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/4/input',
                   headers={'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

draws = res.text.split('\n')[0].split(',')
boards = res.text[:-2].split('\n\n')[1:]

boards = list(map(lambda b: b.split('\n'), boards))

for board in boards:
    for row in board:
        board[board.index(row)] = row = row.split()


def check_board(grid):
    if not grid:
        return False
    for grid_row in grid:
        if len(list(filter(lambda s: s == -1, grid_row))) == 5:
            return True
    for x in range(5):
        col = []
        for y in range(5):
            col.append(grid[y][x])
        if len(list(filter(lambda s: s == -1, col))) == 5:
            return True


def find_winner(grids, numbers):
    winningBoards = []
    for num in numbers:
        for i in (range(len(grids))):
            for grid_row in grids[i]:
                if num in grid_row:
                    grid_row[grid_row.index(num)] = -1
            if check_board(grids[i]):
                winningBoards.append([grids[i], num])
                grids[i] = []

    return winningBoards


winners = find_winner(boards, draws)

unmarked = list(filter(lambda x: x != -1, sum(winners[-1][0], [])))

score = sum(map(lambda x: int(x), unmarked)) * int(winners[-1][1])

print(score)
