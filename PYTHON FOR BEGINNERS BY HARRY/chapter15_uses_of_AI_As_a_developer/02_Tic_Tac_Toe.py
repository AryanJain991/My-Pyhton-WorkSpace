# Here is a step-by-step breakdown of how to create a Tic Tac Toe game in Python, with each step explained as a comment. You can follow these steps to implement the game:

# Step 1: Define the game board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Step 2: Display the board
def display_board(board):
    for row in board:
        print("|".join(row)) 
        print("-" * 5)

# Step 3: Player input
def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

# Step 4: Check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Step 5: Check for a draw
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Step 6: Switch turns
def switch_player(current_player):
    return "O" if current_player == "X" else "X"

# Step 7: Game loop
def play_game():
    board = create_board()
    current_player = "X"
    while True:
        display_board(board)
        player_input(board, current_player)
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        current_player = switch_player(current_player)

# Step 8: Restart option
while True:
    play_game()
    restart = input("Do you want to play again? (yes/no): ").lower()
    if restart != "yes":
        print("Thanks for playing!")
        break


