"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request, url_for, redirect, flash, Markup
from cleanup import read_file
from markov import MarkovChain
import twitter

app = Flask(__name__)
app.secret_key = 'super secret key'

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
    walk = markov_chain.walk_chain()
    lst_to_str = ""
    for i in range(0, len(walk)):
        if i == 0:
            lst_to_str += f'{walk[i].capitalize() } '
        else:
            lst_to_str += f'{walk[i] } '
    return render_template('index.html', message=lst_to_str)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    print(status)
    twitter.tweet(status)
    flash(Markup('Successfully tweeted <a href="https://twitter.com/FlatEarthGnratr" class="alert-link">here</a>'))
    return redirect(url_for('home'))

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True, port=5001)
