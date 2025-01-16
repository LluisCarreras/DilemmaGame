from flask import Flask, render_template, request, jsonify
from lib.dilemma_game import play_a_game


new_game = play_a_game()

app = Flask(__name__)

# turn = new_game.get_round()
# p1_score = new_game._player_0.get_points()
# p2_score = new_game._player_1.get_points()

def create_json (message, the_turn, value_p1, value_p2, score_p1, score_p2):
    return jsonify({'message': message,
                    'value_turn': the_turn,
                    'value_p1': value_p1,
                    'value_p2': value_p2,
                    'score_p1': score_p1,
                    'score_p2': score_p2})

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

@app.route('/guess', methods=['POST'])
def guess():

    global new_game
    # global p1_score
    # global p2_score
    new_game.play_2()

    message = new_game.get_message()
    turn = new_game.get_round()
    p1_value = new_game._player_0.get_points_to_add()
    p2_value = new_game._player_1.get_points_to_add()
    p1_score = new_game._player_0.get_points()
    p2_score = new_game._player_1.get_points()

    return create_json(message, turn, p1_value, p2_value, p1_score, p2_score)

    # does_cooperate = int(request.json['guess'])  
    # turn += 1 
    # if does_cooperate: 
    #     message = 'Cooperates!!!'
    #     p1_value = 1
    #     p2_value = 0
    #     p1_score += p1_value
    #     p2_score += p2_value
    #     return create_json(message, turn, p1_value, p2_value, p1_score, p2_score)
    # else:
    #     message = 'Defects!'
    #     p1_value = 0
    #     p2_value = 1
    #     p1_score += p1_value
    #     p2_score += p2_value
    #     return create_json(message, turn, p1_value, p2_value, p1_score, p2_score)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
