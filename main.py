matrix = [[],[],[]]

def check_status(matrix):
    for row in range(3): #check rows
        if sum(matrix[row]) == 3:
            return "the guy with the X's won"
        elif sum(matrix[row]) == 0:
            return "the guy with the O's won"

    for col in range(3): #check cols
        if matrix[0][col] + matrix[1][col] + matrix[2][col] == 3:
            return "the guy with the X's won"
        elif matrix[0][col] + matrix[1][col] + matrix[2][col] == 0:
            return "the guy with the O's won"

    # diags
    main_diag = matrix[0][0] + matrix[1][1] + matrix[2][2]
    secondary_diag = matrix[0][2] + matrix[1][1] + matrix[2][0]
    if main_diag == 3 or secondary_diag == 3:
        return "the guy with the X's won"
    if main_diag == 0 or secondary_diag == 0:
        return "the guy with the O's won"


def is_legal_move(i,j):
    if matrix[i][j] != -1:
        return "the move is illegal ya samdan"


