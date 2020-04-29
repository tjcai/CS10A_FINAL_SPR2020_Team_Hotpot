from random import*
import time
card=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
suits = ['']

value=[11,10,10,10,10,9,8,7,6,5,4,3,2]


print("The banker is dealing the card……")
time.sleep(2)
computer1=randint(0,12)
computer2=randint(0,12)
print("The banker's cards are: *",card[computer2])
user1=randint(0,12)
user2=randint(0,12)
print("Your cards are:", card[user1],card[user2])
b=input("One more card? Yes or No:")
if b.lower()=="yes":
    user3=randint(0,12)
    print("Your cards now are:", card[user1],card[user2],card[user3])
    total_computer=value[computer1]+value[computer2]
    total_user=value[user1]+value[user2]+value[user3]
    if total_user>21:
        print("You Lose!")
    if total_user<21:
        if total_user > total_computer :
            print("You Win!")
        elif total_user == total_computer:
            print("Tie.")
        else:
            print("You Lose!")


if b.lower()=="no":
    total_computer=value[computer1]+value[computer2]
    total_user=value[user1]+value[user2]
    if total_user>21:
        print("You Lose!")
    if total_user<21:
        if total_user > total_computer :
            print("You Win!")
        elif total_user == total_computer:
            print("Tie.")
        else:
            print("You Lose!")
