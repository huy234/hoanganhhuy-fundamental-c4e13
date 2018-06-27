
count=0
loop = True


from random import randint
numb = randint(1,100)

while loop:
    guess= int(input("Guess my number:  "))
    if guess < numb: 
        print("Too small")
    elif guess > numb:
        print("Too big")
    else:
        print("Bingo")
        break
    count += 1
    if count == 7:
        loop = False
        print("Out of tries")