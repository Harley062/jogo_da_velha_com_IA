import random

def print_board(board):
    print("  0 1 2")
    print(" ┌─┬─┬─┐")
    for r, row in enumerate(board):
        print(f"{r}│{'│'.join(row)}│")
        if r < 2:
            print(" ├─┼─┼─┤")
    print(" └─┴─┴─┘")

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  
        [board[1][0], board[1][1], board[1][2]],  
        [board[2][0], board[2][1], board[2][2]],  
        [board[0][0], board[1][0], board[2][0]],  
        [board[0][1], board[1][1], board[2][1]],  
        [board[0][2], board[1][2], board[2][2]],  
        [board[0][0], board[1][1], board[2][2]],  
        [board[2][0], board[1][1], board[0][2]]   
    ]
    return [player, player, player] in win_conditions

def get_empty_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -10
    if check_winner(board, 'O'):
        return 10
    if not get_empty_positions(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for row, col in get_empty_positions(board):
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row, col in get_empty_positions(board):
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for row, col in get_empty_positions(board):
        board[row][col] = 'O'
        score = minimax(board, 0, False)
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            move = (row, col)
    return move

def player_move(board):
    while True:
        try:
            position = input("Digite a posição (ex: 00 para linha 0, coluna 0): ")
            row, col = int(position[0]), int(position[1])
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("A posição já está ocupada. Tente novamente.")
        except (IndexError, ValueError):
            print("Entrada inválida. Digite uma posição válida no formato 'linha coluna'.")

def ai_move(board):
    move = best_move(board)
    if move:
        row, col = move
        board[row][col] = 'O'

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Bem-vindo ao Jogo da Velha!")
    
    while True:
        print_board(board)
        player_move(board)
        if check_winner(board, 'X'):
            print_board(board)
            print("Você venceu!")
            break
        if not get_empty_positions(board):
            print_board(board)
            print("Empate!")
            break

        ai_move(board)
        if check_winner(board, 'O'):
            print_board(board)
            print("A IA venceu!")
            break
        if not get_empty_positions(board):
            print_board(board)
            print("Empate!")
            break

if __name__ == "__main__":
    main()
