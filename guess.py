import random

print("Number Guessing Game")
print("Guess a Number between 1 to 9")
count = 0
number = random.randint(1,10)
while count < 5 :
    guess = int(input("enter your number:"))
    if (guess == number):
        print("you won the game")
    elif (guess > number):
        print("guess a smaller number than",number+2)   
        count = count+1
    else:
        print("guess a bigger number bigger than",number-2)
        count = count+1
if (count == 5):
    print("You Lose","the number was",number)        
