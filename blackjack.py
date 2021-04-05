from random import randrange
#BLACKJACK
meno = input("Zadajte vaše použivatelské meno: ")
score = 0
score2 = 0
score = score + (randrange(1,11))
print(meno, "má", score)
score2 = score2 + (randrange(1,11))
print("Počitač má", score2)

while score < 21:
    odpoved = str(input("Chceš hitnut alebo zostat? "))
    if odpoved == "hit":
        score = score + (randrange(1,11))
        print("Teraz máš", score)
    else:
        if score2 < score:
            score2 = score2 + (randrange(1,11))
            print("Dealer si tahá ...")
        if score2 < score:
            score2 = score2 + (randrange(1,11))
            print("Dealer si tahá ...")
        if score2 < score:
            score2 = score2 + (randrange(1,11))
            print("Dealer si tahá ...")
        print("Dealer má", score2)
        print(meno, "má", score)
        if score2 > score and score2 <= 21:
            print("Dealer vyhral!", score2)
        else:
            print(meno, "vyhral !", score)
            
        break

if score > 21:
    print("Prehral si! Dealer vyhral.")

elif score == 21:
    print("Máš BLACKJACK!")

if score == score2:
    print(score, "a", score2, "remíza")
