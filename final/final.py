from flask import Flask, render_template, request
from Deck import Deck
import hangman_app
import random
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
Bellow are codes of hangman game
"""
@app.route('/hangman')
def hangman():
    return render_template("hangman.html")

state = {'guesses':[],
        'word':"interesting",
        'word_so_far':"-",
        'done':False,
        "chances":10,
        "response":" ",
        "one_more_time":" ",
        "stat":" "}

@app.route('/hangman/start')
def hangman_start():
    global state
    state = {'guesses':[],
            'word':"interesting",
            'word_so_far':"-",
            'done':False,
            "chances":10,
            "response":" ",
            "one_more_time":" ",
            "stat":" "}
    state['word']=hangman_app.generate_random_word()
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
                state['stat'] = 'win'
                state['done'] = True
            elif state['chances'] == 0:
                state['response'] = "You have used up your chances. The word is: %s" % state['word']
                state["one_more_time"] = "Hit the red NEW GAME button for another game"
                state['stat'] = 'lose'
                state['done'] = True
            if state['done'] == True:
                return render_template('hangman_end.html',state=state)
            else:
                return render_template('hangman_play.html',state=state)


"""
Below are codes for chatbot
"""
@app.route('/chatbot')
def chat_bot():
    return render_template("chat_bot.html")

list = ["hangman","blackjack","guess the number","book of answers"]

@app.route('/chatbot/start')
def chatbot_start():
    return render_template('chatbot_start.html') #why state=state?  ,state=state

@app.route('/chatbot/play',methods=['GET','POST'])
def chatbot_play():
    global list
    if request.method == 'GET':
        return chatbot_start()
    elif request.method == 'POST':
        game = request.form['game'].lower()
        if game in list:
            stipped = game.strip(" ")
            wo_li = stipped.split(" ")
            n = ''
            for i in range(len(wo_li)-1):
                n += (wo_li[i] + '_')
            n += wo_li[-1]
            link = n + '_start'
            return render_template('chatbot_play.html', link=link, game=game)
        else:
            guidance = 'Please input correct name of games!'
            return render_template('chatbot_start.html', guidance = guidance)

"""
Below are codes for guessing a number
"""
state2 = {'guesses':[],
        'number':0,
        'done':False,
        "chances":7,
        "response":" ",
        "one_more_time":" "}

@app.route('/guess_the_number')
def guess_the_number():
    global state2
    return render_template("guess_the_number.html")

@app.route('/guess_the_number/start')
def guess_the_number_start():
    global state2
    state2 = {'guesses':[],
            'number':0,
            'done':False,
            "chances":7,
            "response":" ",
            "one_more_time":" "}
    state2['number']=random.randint(0,100)
    return render_template('guess_the_number_start.html')

@app.route('/guess_the_number/play',methods=['GET','POST'])
def guess_the_number_play():
    global state2
    if request.method == 'GET':
        return guess_the_number_start()
    elif request.method == 'POST':
        while not state2['done']:
            n = request.form['guessn']
            if n in state2['guesses']:
                state2['response'] = "You have guessed this number. Try a new one."
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
            else:
                state['reponse'] = "Please input numbers to guess"
                state2['chances'] -= 1

            if int(n) == state2['number']:
                state2['response'] = "Congradulations! You have guessed the number! The number is: %s" % state2['number']
                state2["one_more_time"] = "Hit the red NEW GAME button for another game"
                state2['done'] = True
                return render_template('guess_the_number_end_1.html',state2=state2)
            elif state2['chances'] == 0:
                state2['response'] = "You have used up your chances. The number is: %s" % state2['number']
                state2["one_more_time"] = "Hit the red NEW GAME button for another game"
                state2['done'] = True
            if state2['done'] == True:
                return render_template('guess_the_number_end_2.html',state2=state2)
            else:
                return render_template('guess_the_number_play.html',state2=state2)

@app.route('/guess_the_number/method')
def guess_the_number_method():
    return render_template("guess_the_number_method.html")


"""
Below are codes of Book of Arts
"""
texts=['Do Not Bet On It','Deal With It Later','It is Significant','Move On','Do not Hesitate','Speak Up About It','Approach Cautiously','Focus On Your Home Life','Investigate And Enjoy It','Definitely','Absolutely Not','Better To Wait','It Seems Assured','Do It Early','Keep It To Yourself','Doubt It','Be Patient','Get It In Writing','Avoid The First Solution','Remain Flexible']

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
        if a.lower() == 'yes':
            b = random.randint(0,19)
            out = texts[b]
            return render_template('book_of_answers_play.html', out = out)
        else:
            surprise = '----Welcome back to our main page! Surprise!----'
            return render_template('main.html',surprise = surprise)

"""
Below are codes for an easy version of blackjack
"""

bj = {'computer':[],'user':[],
        'c_r':'','u_r':'',
        'c_v':[],'u_v':[],
        'done':False,'result':'',
        'counter':1,'hidden':'',
        'c_p':0, 'u_p':0,'stat':' '} #computer response, user reponse

@app.route('/blackjack')
def blackjack():
    return render_template("blackjack.html")

@app.route('/blackjack/start')
def blackjack_start():
    global bj
    bj = {'computer':[],'user':[],
            'c_r':'','u_r':'',
            'c_v':[],'u_v':[],
            'done':False,'result':'',
            'counter':1,'hidden':'',
            'c_p':0, 'u_p':0, 'stat':' '} # c_p is for computer points
    global card
    global value
    card=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    value=[11,10,10,10,10,9,8,7,6,5,4,3,2]
    computer1=random.randint(0,12)
    computer2=random.randint(0,12)
    bj['computer'].append(card[computer1])
    bj['computer'].append(card[computer2])
    bj['c_v'].append(value[computer1])
    bj['c_v'].append(value[computer2])
    bj['hidden'] = card[computer1]
    bj['c_r'] = "The dealer's cards are: * " + card[computer2]
    user1=random.randint(0,12)
    user2=random.randint(0,12)
    bj['user'].append(card[user1])
    bj['user'].append(card[user2])
    bj['u_v'].append(value[user1])
    bj['u_v'].append(value[user2])
    bj['u_r'] = "Your cards are: " + card[user1] + ' ' + card[user2]
    bj['c_p'] = sum(bj['c_v'][1:])
    bj['u_p'] = sum(bj['u_v'])
    if sum(bj['c_v']) <= 21 and sum(bj['u_v']) <= 21:
        bj = bj
    elif sum(bj['c_v']) >= 21 and sum(bj['u_v']) >= 21:
        bj['result'] = "Tie"
        bj['stat'] = 't'
    elif sum(bj['c_v']) >= 21:
        bj['result'] = "You Win!"
        bj['stat'] = 'w'
    else:
        bj['result'] = "You Lose!"
        bj['stat'] = 'l'
    return render_template("blackjack_start.html",bj = bj)


@app.route('/blackjack/play',methods = ['GET','POST'])
def blackjack_play():
    global bj
    if request.method == 'GET':
        return blackjack_start()
    elif request.method == 'POST':
        while not bj['done']:
            reply = request.form['one_more_card']

            if reply.lower() == 'yes':
                bj['counter'] += 1
                global card
                global value
                if sum(bj['c_v']) < 17:
                    computer3 = random.randint(0,12)
                    bj['computer'].append(card[computer3])
                    bj['c_v'].append(value[computer3])
                    c = ' ' + card[computer3]
                    bj['c_r'] += c

                user3 = random.randint(0,12)
                bj['user'].append(card[user3])
                bj['u_v'].append(value[user3])
                d = ' ' + card[user3]
                bj['u_r'] += d

                if sum(bj['c_v']) <= 21 and sum(bj['u_v']) <= 21:
                    bj['c_p'] = sum(bj['c_v'][1:])
                    bj['u_p'] = sum(bj['u_v'])
                    return render_template("blackjack_play.html",bj=bj)
                elif sum(bj['c_v']) >= 21 and sum(bj['u_v']) <= 21:
                    bj['result'] = "You win!"
                    bj['stat'] = 'w'
                else:
                    bj['result'] = "You lose!"
                    bj['stat'] = 'l'
                bj['c_r'] = "The dealer's cards are: " + bj['hidden'] +' '+ bj['c_r'][26:]
                bj['c_p'] = sum(bj['c_v'])
                bj['u_p'] = sum(bj['u_v'])
                return render_template("blackjack_end.html",bj = bj)

            else:
                while sum(bj['c_v']) < 17:
                    computer3 = random.randint(0,12)
                    bj['computer'].append(card[computer3])
                    bj['c_v'].append(value[computer3])
                    c = ' ' + card[computer3]
                    bj['c_r'] += c
                if sum(bj['c_v']) > 21:
                    bj['result'] = "You win!"
                    bj['c_p'] = sum(bj['c_v'])
                    bj['u_p'] = sum(bj['u_v'])
                    bj['stat'] = 'w'
                    return render_template("blackjack_end.html",bj = bj)
                bj['done'] = True


        if sum(bj['c_v']) <= 21 and sum(bj['u_v']) <= 21:
            if sum(bj['c_v']) >= sum(bj['u_v']):
                bj['result'] = "You Lose!"
                bj['stat'] = 'l'
            else:
                bj['result'] = "You Win!"
                bj['stat'] = 'w'
        elif sum(bj['c_v']) >= 21 and sum(bj['u_v']) <= 21:
            bj['result'] = "You Win!"
            bj['stat'] = 'w'
        else:
            bj['result'] = "You Lose!"
            bj['stat'] = 'l'

        bj['c_r'] = "The dealer's cards are: " + bj['hidden'] +' '+ bj['c_r'][26:]
        bj['u_p'] = sum(bj['u_v'])
        bj['c_p'] = sum(bj['c_v'])
        return render_template("blackjack_end.html",bj = bj)


if __name__ == '__main__':
    app.run(debug = True)
