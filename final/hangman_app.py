"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

def generate_random_word():
    file = open("wordlist_raw.txt","r")
    text = file.read()
    """
    wordlist = list()
    for line in file:
        line1 = line.split(" ")[0]
        wordlist.append(line1.strip())
    """
    wordlist = text.split("\n")
    from random import choice
    word = choice(wordlist)
    return word.lower()

def play_hangman():
    one_more_time = True

    while one_more_time:
        guessed_letters = []
        guess_left = 6
        word = generate_random_word()
        word_li = list(word)
        done = False

        raw = []
        for a in range(len(word_li)):
            raw.append('-')

        while not done:

            print("-----------")
            print(raw)
            print(guess_left, "chances left")
            guess = input("pick a letter: ")

            if guess in guessed_letters:
                """Repeated guessing"""
                guess_left -= 1
                print("You've already guessed this letter. Try a new one.")

            elif guess not in word_li:
                """Wrong guess"""
                guess_left -= 1
                guessed_letters.append(guess)
                print("This letter is not in the word. Please try a new one")

            elif guess in word_li:
                """Correct Guess"""
                counter = -1
                for i in word:
                    counter += 1
                    if guess == i:
                        raw[counter] = i
                guess_left = guess_left
                guessed_letters.append(guess)

            if raw == word_li:
                """Correct Guess."""
                print(raw)
                print("Congratualation! You won!")
                done = True
            elif guess_left == 0:
                """No more chances."""
                print(raw)
                print("Sorry, you have used up all the chances.")
                print("The word is: ",word)
                done = True

        """Ask whether to play another game."""
        one_more_time = input("Do you want to play again? [Y]es or [N]o")
        if one_more_time.upper() == "Y":
            one_more_time = True
        else:
            one_more_time = False

if __name__ == '__main__':
    play_hangman()
