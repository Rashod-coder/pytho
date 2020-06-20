import random
import time
    
guess_count = 1
guess_limit = 7
out_of_tries = False
number = random.randint(1,100)
yeet = ['yes','yes']
yeetus = ['quit', 'quit']

secretChoice = random.choice(yeet)
secretChoice2 = random.choice(yeetus)



print("Welcome to the guessing game guess a number between 1 and 100 you get 10 tries or else you lose.")
time.sleep(1)
print(number)
guess = int(input("Guess a number between 1 and 100 "))
while guess !=quit:
    while guess !=number and not(out_of_tries):
        if guess_count < guess_limit:   
            guess_count += 1  
        else:
            out_of_tries = True
        if guess > number:
            print(guess, "was to high")

        if guess < number:
            print(guess, "was to low try again")
        guess = int(input("Guess again: "))
    if out_of_tries:
        print("Ran out of tries YOU lose the number was", number)
    else: 
        print(guess, "was the number! You win!")
    print()
    user4 = input("Do you want to play again enter (yes) to play again or enter (quit) to stop playing: ")
    if user4 == secretChoice:
         guess = int(input("Guess a number between 1 and 100 "))
         number = random.randint(1,100) #randomizes a number between 1 and 100      
       

    if user4 == secretChoice2:
        print("Thanks for playing")
        break

     
    
 

 






