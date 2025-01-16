import random
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# Generate the number to guess
#number = random.randint(1, 100)

turn = 0

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

@app.route('/guess', methods=['POST'])
def guess():
    global turn
    does_cooperate = int(request.json['guess'])  
    turn += 1 
    if does_cooperate: 
        return jsonify({'message': 'Cooperates!!!',
                        'value_turn': turn,
                        'value_player_1': 1,
                        'value_player_2': 0})
    else:
        return jsonify({'message': 'Defects!',
                        'value_turn': turn,
                        'value_player_1': 0,
                        'value_player_2': 1})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
