#!/usr/bin/python

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize the game matrix
matrix = [[0,0,0], [0,0,0], [0,0,0]]

def check_status(matrix):
    for row in range(3):  # check rows
        if sum(matrix[row]) == 3:
            return "the guy with the X's won"
        elif sum(matrix[row]) == -3:
            return "the guy with the O's won"

    for col in range(3):  # check cols
        if matrix[0][col] + matrix[1][col] + matrix[2][col] == 3:
            return "the guy with the X's won"
        elif matrix[0][col] + matrix[1][col] + matrix[2][col] == -3:
            return "the guy with the O's won"

    # diagonals
    main_diag = matrix[0][0] + matrix[1][1] + matrix[2][2]
    secondary_diag = matrix[0][2] + matrix[1][1] + matrix[2][0]
    if main_diag == 3 or secondary_diag == 3:
        return "the guy with the X's won"
    if main_diag == -3 or secondary_diag == -3:
        return "the guy with the O's won"

    return "continue playing"

def is_legal_move(i, j):
    if matrix[i][j] != 0:
        return False
    return True



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    i, j, player = data['i'], data['j'], data['player']
    
    if is_legal_move(i, j):
        matrix[i][j] = player
        status = check_status(matrix)
        return jsonify({"status": status})
    else:
        return jsonify({"status": "Illegal move"}), 400

if __name__ == '__main__':
    app.run(debug=True)
