"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from cleanup import read_file
from markov import MarkovChain

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    word_list = read_file('example_txt/flat_earth.txt')
    # histogram = Dictogram(word_list)
    markov_chain = MarkovChain(word_list, 15)
    return markov_chain

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    markov_chain = before_first_request()
    walk = markov_chain.walk_chain(50)
    lst_to_str = ""
    for i in walk:
        lst_to_str += f'{i} '
    return render_template('index.html', message=lst_to_str)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True, port=5001)
