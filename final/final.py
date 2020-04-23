from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/team_bio')
def team_bio():
    return render_template("team_bio.html")

"""
Bellow are the codes of hangman game
"""
@app.route('/hangman')
def hangman():
    return render_template("hangman.html")

global state
state = {'guesses':[],
        'word':"interesting",
        'word_so_far':"-",
        'done':False,
        "chances":6,
        "response":" ",
        "one_more_time":" "}

@app.route('/hangman/start')
def hangman_start():
    global state
    state['word']=hangman_app.generate_random_word()
    state['guesses'] = []
    l = len(state['word'])
    b = '-'*l
    state['word_so_far'] = b
    return render_template("hangman_start.html",state=state)

@app.route('/hangman/play',methods=['GET','POST'])
def hangman_play():
    global state
    if request.method == 'GET':
        return hangman_start()
    elif request.method == 'POST':

        while not state['done']:
            letter = request.form['guess']
            if letter in state['guesses']:
                state['response'] = "You have guessed this letter. Try a knew one."
                state['chances'] -= 1
            elif letter in state['word']:
                s = []
                for n in state['word_so_far']:
                    s += [n]
                counter = -1
                for i in state['word']:
                    counter += 1
                    if i == letter:
                        s[counter] = i
                state['word_so_far'] = "".join(s)
                state['chances'] = state['chances']
                state['response'] = "This is a correct letter!"
                state['guesses'] += [letter]
            elif letter not in state ['word']:
                state['response'] = "You have guessed wrong. Try another letter."
                state['chances'] -= 1
                state['guesses'] += [letter]

            if state['word_so_far'] == state['word']:
                state['response'] = "You have guessed the word! The word is: %s" % state['word']
                state['done'] = True
            elif state['chances'] == 0:
                state['response'] = "You have used up your chances. The word is: %s" % state['word']
                state["one_more_time"] = "hit the red NEW GAME button for another game"
                state['done'] = True
            return render_template('hangman_play.html',state=state)



@app.route('/blackjack')
def blackjack():
    return render_template("blackjack.html")


@app.route('/blackjack/start')
def blackjack_start():
    return render_template("blackjack_start.html")






if __name__ == '__main__':
    app.run(debug = True)
