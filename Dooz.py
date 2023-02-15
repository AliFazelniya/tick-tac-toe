rows = int(input("Please enter the number of rows: "))
def board():
    matrix0 = []
    for i in range(rows):
        list0 = []
        for j in range(rows):
            list0.append(0)
        matrix0.append(list0)
    return matrix0
Main_board = board()
def show_board(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print("")
show_board(Main_board)
def user_choice(board):
    choice = input("Enter a part: ").split(",")
    choice = list(map(int, choice))
    i = choice[0]
    j = choice[1]
    if board[i][j] == 0:
        board[i][j] = "U"
        show_board(board)
    else:
        print("The part has been chosen.")
        user_choice(Main_board)
def com_choice(board):
    first_choice = random.choice(range(rows))
    second_choice = random.choice(range(rows))
    t = first_choice
    z = second_choice
    if board[t][z] == 0:
        board[t][z] = "C"
        show_board(board)
    else:
        com_choice(Main_board)
com_win_list = []
user_win_list = []
def check_win_rows(board):
    for i in board:
        com_win_list.clear()
        user_win_list.clear()
        for j in range(rows):
            if i[j] == "C":
                com_win_list.append(i[j])
            if i[j] == "U":
                user_win_list.append(i[j])
        if len(com_win_list) == rows:
            print("Computer won!")
            exit()
        elif len(user_win_list) == rows:
            print("User won!")
            exit()
    else:
        return False
def check_win_diameter(board):
    com_win_list.clear()
    user_win_list.clear()
    for i in range(rows):
        for j in range(rows):
            if i == j:
                if board[i][j] == "U":
                    user_win_list.append(board[i][j])
                if board[i][j] == "C":
                    com_win_list.append(board[i][j])
    if len(com_win_list) == rows:
        print("Computer won!")
        exit()
    elif len(user_win_list) == rows:
        print("User won!")
        exit()
    else:
        return False
def check_win_columns(board):
    for i in range(rows):
        user_win_list.clear()
        com_win_list.clear()
        for j in range(rows):
            if board[j][i] == "U":
                user_win_list.append(board[i][j])
            if board[j][i] == "C":
                com_win_list.append(board[i][j])
        if len(com_win_list) == rows:
            print("Computer won!")
            exit()
        elif len(user_win_list) == rows:
            print("User won!")
            exit()
    else:
        return False
def check_win_subdiameter(board):
    start = 0
    com_win_list.clear()
    user_win_list.clear()
    for i in range(1,rows+1):
        if board[i-1][rows-i] == "U":
            user_win_list.append(board[i-1][rows-i])
        if board[i-1][rows-i] == "C":
            com_win_list.append(board[i-1][rows-i])
    if len(com_win_list) == rows:
        print("Computer won!")
        exit()
    elif len(user_win_list) == rows:
        print("User won!")
        exit()
    else:
        return False
def win_possibilities(board):
    check_win_rows(board)
    check_win_columns(board)
    check_win_diameter(board)
    check_win_subdiameter(board)
chances = 0
while chances < rows*rows:
    user_choice(Main_board)
    chances += 1
    win_possibilities(Main_board)
    if chances < rows*rows:
        com_choice(Main_board)
        chances += 1
    win_possibilities(Main_board)
else:
    if check_win_rows(Main_board)== False and check_win_diameter(Main_board)== False and check_win_columns(Main_board) == False and check_win_subdiameter(board) == False :
        print("Draw")