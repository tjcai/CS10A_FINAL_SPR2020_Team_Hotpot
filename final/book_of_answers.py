from random import *

A=input("Think one question silently. Ready for your answer? Yes or No:")
texts=['Do Not Bet On It','Deal With It Later','It is Significant','Move On','Do not Hesitate','Speak Up About It','Approach Cautiously','Focus On Your Home Life','Investigate And Enjoy It','Definitely','Absolutely Not','Better To Wait','It Seems Assured','Do It Early','Keep It To Yourself','Doubt It','Be Patient','Get It In Writing','Avoid The First Solution','Remain Flexable']
while A.lower()=="yes":
    a=randint(0,19)
    print(texts[a])
    l=input("Want to play again? Yes or No:")
    if l.lower()=="yes":
        continue
    if l.lower()=="no":
        break
    

 
   
   
   
    



