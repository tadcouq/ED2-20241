import math

# Đại diện cho người chơi
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'
EMPTY = '_'

# Kiểm tra xem có ai thắng chưa
def check_winner(board):
    win_states = [
        [board[0], board[1], board[2]],  # Hàng ngang
        [board[3], board[4], board[5]], 
        [board[6], board[7], board[8]], 
        [board[0], board[3], board[6]],  # Cột dọc
        [board[1], board[4], board[7]], 
        [board[2], board[5], board[8]], 
        [board[0], board[4], board[8]],  # Đường chéo
        [board[2], board[4], board[6]]
    ]
    if [AI_PLAYER] * 3 in win_states:
        return 1  # AI thắng
    elif [HUMAN_PLAYER] * 3 in win_states:
        return -1  # Người thắng
    elif EMPTY not in board:
        return 0  # Hòa
    return None  # Chưa kết thúc

# Hàm Minimax
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner is not None:
        return winner  # Trả về điểm số nếu có người thắng hoặc hòa

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI_PLAYER
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY  # Hoàn tác
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN_PLAYER
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(best_score, score)
        return best_score

# Hàm chọn nước đi tốt nhất cho AI
def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI_PLAYER
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move

# Ví dụ bảng cờ hiện tại
board = [
    'X', 'O', 'X',
    'O', 'X', 'O',
    '_', '_', '_'
]

# AI tìm nước đi tốt nhất
best_position = best_move(board)
print("AI chọn ô:", best_position)
