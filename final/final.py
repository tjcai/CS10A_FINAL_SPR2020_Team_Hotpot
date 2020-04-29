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
                state['response'] = "You have guessed the word! Congradulations! The word is: %s" % state['word']
                state['done'] = True
            elif state['chances'] == 0:
                state['response'] = "You have used up your chances. The word is: %s" % state['word']
                state["one_more_time"] = "hit the red NEW GAME button for another game"
                state['done'] = True
            if state['done'] == True:
                return render_template('hangman_end.html',state=state)
            else:
                return render_template('hangman_play.html',state=state)



@app.route('/blackjack')
def blackjack():
    return render_template("blackjack.html")


@app.route('/blackjack/start')
def blackjack_start():
    return render_template("blackjack_start.html")

"""
Below are codes for chatbot
"""

@app.route('/chatbot')
def chat_bot():
    return render_template("chat_bot.html")

list = ["hangman","blackjack","guessing"]

@app.route('/chatbot/start')
def chatbot_start():
    global list
    return render_template('chatbot_start.html') #why state=state?  ,state=state

@app.route('/chatbot/play',methods=['GET','POST'])
def chatbot_play():
    global list
    if request.method == 'GET':
        return chatbot_start()
    elif request.method == 'POST':
        game = request.form['game']
        for i in list:
            if i == game:
                stipped = i.strip(" ")
                link = stipped + '_start'
    return render_template('chatbot_play.html', link=link, game=game)

"""
Below are codes for guessing a number
"""
import random

state2 = {'guesses':[],
        'number':0,
        'done':False,
        "chances":5,
        "response":" ",
        "one_more_time":" "}

@app.route('/guessing')
def guessing():
    global state2
    return render_template("guessing.html")

@app.route('/guessing/start')
def guessing_start():
    global state2
    state2['number']=random.randint(0,100)
    return render_template('guessing_start.html')

@app.route('/guessing/play',methods=['GET','POST'])
def guessing_play():
    global state2
    if request.method == 'GET':
        return guessing_start()
    elif request.method == 'POST':
        while not state2['done']:
            n = request.form['guessn']
            if n in state2['guesses']:
                state2['response'] = "You have guessed this number. Try a knew one."
                state2['chances'] -= 1
            elif int(n) < state2['number']:
                state2['chances'] -= 1
                state2['response'] = "Your guess is too small!"
                state2['guesses'].append(n)
            elif int(n) > state2['number']:
                state2['response'] = "You have guessed wrong. Try another letter."
                state2['chances'] -= 1
                state2['response'] = "Your guess is too large!"
                state2['guesses'].append(n)

            if int(n) == state2['number']:
                state2['response'] = "You have guessed the number! Congradulations! The number is: %s" % state2['number']
                state2["one_more_time"] = "hit the red NEW GAME button for another game"
                state2['done'] = True
            elif state2['chances'] == 0:
                state2['response'] = "You have used up your chances. The number is: %s" % state2['number']
                state2["one_more_time"] = "hit the red NEW GAME button for another game"
                state2['done'] = True
            if state2['done'] == True:
                return render_template('guessing_end.html',state2=state2)
            else:
                return render_template('guessing_play.html',state2=state2)

    return render_template('guessing_play.html', state2=state2, n=n)

"""
Below are codes of Book of Arts
"""
texts=['Do Not Bet On It','Deal With It Later','It is Significant','Move On','Do not Hesitate','Speak Up About It','Approach Cautiously','Focus On Your Home Life','Investigate And Enjoy It','Definitely','Absolutely Not','Better To Wait','It Seems Assured','Do It Early','Keep It To Yourself','Doubt It','Be Patient','Get It In Writing','Avoid The First Solution','Remain Flexable']

@app.route('/book_of_answers')
def book_of_answers():
    return render_template('book_of_answers.html')

@app.route('/book_of_answers/start')
def book_of_answers_start():
    return render_template('book_of_answers_start.html')

@app.route('/book_of_answers/play',methods=['GET','POST'])
def book_of_answers_play():
    global texts
    if request.method == 'GET':
        return book_of_answers_start()
    elif request.method == 'POST':
        a = request.form['answer']
        if a == 'yes':
            b = random.randint(0,19)
            out = texts[b]
            return render_template('book_of_answers_play.html', out = out)
        else:
            surprise = 'Welcome back to our main page! Surprise!'
            return render_template('main.html',surprise = surprise)



if __name__ == '__main__':
    app.run(debug = True)
