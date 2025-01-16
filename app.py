from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Generate the number to guess
number = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

@app.route('/guess', methods=['POST'])
def guess():
    global number
    guess = int(request.json['guess'])  # Get the guess from the client
    if guess < number:
        return jsonify({'message': 'Too low!'})
    elif guess > number:
        return jsonify({'message': 'Too high!'})
    else:
        number = random.randint(1, 100)  # Reset the number for a new game
        return jsonify({'message': 'Congratulations! You guessed it!'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
