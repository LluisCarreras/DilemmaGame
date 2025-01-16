import random
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# Generate the number to guess
#number = random.randint(1, 100)

turn = 0
player1_score = 0
player2_score = 0

def create_json (message, turn, value_p1, value_p2):
    return jsonify({'message': message,
                    'value_turn': turn,
                    'value_player_1': value_p1,
                    'value_player_2': value_p2})

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

@app.route('/guess', methods=['POST'])
def guess():
    global turn
    global player1_score
    global player2_score
    does_cooperate = int(request.json['guess'])  
    turn += 1 
    if does_cooperate: 
        message = 'Cooperates!!!'
        value_p1 = 1
        value_p2 = 0
        return create_json(message, turn, value_p1, value_p2)
    else:
        message = 'Defects!'
        value_p1 = 0
        value_p2 = 1
        return create_json(message, turn, value_p1, value_p2)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
