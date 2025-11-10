#Mini-Project - Tic Tac Toe


def display_board(board):
    print('*******************')
    for i, row in enumerate(board):
        line = '*'
        for j, cell in enumerate(row):
            symbol = cell if cell != ' ' else ' '
            line += f"  {symbol}  "
            if j < 2:
                line += '|'
        line += '*'
        print(line)
        if i < 2:
            print('*  ---|-----|---  *')
    print('*******************')

def player_input(player, board):
    while True:
        try:
            print(f"{player['name']}'s turn ({player['symbol']})")
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Please enter valid row and column numbers.")
            continue
        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == ' ':
                return (row, col)
            else:
                print("That cell is already taken. Try another.")
        else:
            print("Row and column must be between 1 and 3.")

def check_win(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False

def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = [
        {"name": "Player 1", "symbol": "X"},
        {"name": "Player 2", "symbol": "O"},
    ]
    current = 0
    print("Welcome to Tic Tac Toe!")
    while True:
        display_board(board)
        player = players[current]
        row, col = player_input(player, board)
        board[row][col] = player['symbol']
        if check_win(board, player['symbol']):
            display_board(board)
            print(f"Congratulations! {player['name']} ({player['symbol']}) wins!")
            break
        if check_tie(board):
            display_board(board)
            print("Game over! It's a tie!")
            break
        current = 1 - current

if __name__ == "__main__":
    play()