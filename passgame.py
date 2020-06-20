import random #IMporting the modules required for this program
import time   #IMporting the modules required for this program
import turtle #IMporting the modules required for this program

    
pass_count = 0
max_limit = 12
out_of_chances = False
users =  ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','kiwi', 'grape','orange', 'cherry', 'peach', 'plum','strawberry', 'blueberry' ]

user1 =  ['yes', 'yes', 'yes',]
user2 = ['no', 'no']
user3 = ['yes', 'yes']
user4 = ['no', 'no']


secretWord = random.choice(user1)
secretWord2 = random.choice(user2)
secretWord3 = random.choice(user3)
secretWord4 = random.choice(user4)


player = input("Do you want to play some few games?   Yes or no (The awnser to this question has to be awnswered like this 'yes' or 'no' all lowercase letters): ")
if player == secretWord:
    print("Okay here is a mini game starting soon heres are some basic information:")
    time.sleep(3)


    print("""
      1. You have to guess the password a list of possible awnsers(Remember everytime a diffrent password is generated but the password will be from the list of choices given) 
      2. You get around 5-7 tries if you fail to guess the password access is denied.
      3. All awnsers to every question has to be in lowercase.
      4. If you guess the correct password you get access to a guessing the number game you get 7-9 tries to guess the number
      5. If you enter the correct password you will be asked if you want to play games.
      6. When your playing the guessing game you must enter a integer and no text or else it will kick you out of the game. 
      7. If you type in an incorrect option you will be kicked out of the game(Except when your guessing the password you wont be kicked out of the game it will only kick you when you run out of tries.) """)
    time.sleep(1)

    print("Game starting in 5-7 seconds.")
    time.sleep(5)


    print("Game starting...")
    time.sleep(4)
    print("Enter the password in order to access the fun game. a hint will be given out each game a diffrent password will be generated.")
    time.sleep(1)
    secretWords = random.choice(users)
    time.sleep(3)

    print("""
           These are the possbile passwords: carrot, pear, mango, apple, banana, apricot, pineapple, kiwi, grape, orange, cherry, plum, peach, strawberry, blueberry, rasberry""") 

    password = input("Enter the password >> ")
    while password !=secretWords and not(out_of_chances):
        if pass_count < max_limit:   
             pass_count += 1  
        else:
            out_of_chances = True
 
        if out_of_chances:
            time.sleep(1)

        password = input("Incorrect password try again>>  ")

        if out_of_chances:
            print("Access Denied better luck next time.")
    



    if password == secretWords:
        print()
        print("Access Granted welcome to the guessing game enjoy playing it!!")
        time.sleep(3)
        guess_count = 0
        guess_limit = 8
        out_of_tries = False
        number = random.randint(1,100)
        

        print("""
        Welcome to zee game lab you have diffrent games you could play just type in the game pin which will be revealed soon. 
        Enjoy your experince more games are bound to come!!!! """)
        time.sleep(2)

        
        game2 = input("""
        Do you want play another few games? Yes or no 
        (The awnser to this question has to be awnswered like this 'yes' or 'no' all lowercase letters): """)
        if game2 == secretWord3:
            print("Okay starting game shortly have fun!")

            print("Game options: To choose a game you have to type in the game pin which is next to the name of the game ")

            print("""Options:    
            1. Rock Paper Scissor against Game pin: 245
            2. Decode or Encode a message Game pin: 264
            3. Guessing the number game   Game pin: 454
            4. Random password generator  Game pin: 557 
            5. The magic 8 ball game----->Game pin: 353
            6. TBD Game pin: N/A
            7  TBD Game pin: N/A
            8  TBD Game pin: N/A
            These are all our options for now.""")
            time.sleep(5)
              
            rock = ['245', '245']
            decode = ['264', '264' ]
            guessy = ['454', '454']
            generator = ['557', '557']
            game8ball = ['353', '353']
            game5 = ['374', '374']
            game6 = ['534', '534']
            game7 = ['938', '938']
            game8 = ['645', '645']

            secret = random.choice(rock)
            secret2 = random.choice(decode)
            secret3 = random.choice(guessy)
            secret4 = random.choice(generator)
            secret5 = random.choice(game8ball)
             # secret6 = random.choice()
              #secret7 = random.choice()
              #secret8 = random.choice()

            
            pin_count = 0
            max_tries = 9
            out_of_pin = False
            
            
            
            
            
            
            gamer = input("What game do you want to play? (Has to be out of the game options type in the game pin of the game you want to play to continue to the game)Enter the game pin here:   ")
              
            if gamer == secret:
                print("Okay Starting Rock Paper Scissor Shoot game against computer...")
                time.sleep(2)
                print("Starting game")
                choices = ['paper', 'rock', 'scissor']
                print("HOW TO PLAY: Rock crushes the scissor, Paper would cover rock, and scissor cuts paper")
               
                player3 = input("""Do you want to be rock paper or scissors? (Type in your choices in lowercase for example "paper"): """)
                
                while player3 != "quit":
                    player3 = player3.lower()
            
                    computer = random.choice(choices)
                    print("You have chose " +player3+ ", and the computer has choosen " +computer+ ".")
                    if player3 == computer:
                        print("You have tied with the computer thanks for playing!")
                    elif player3 == "rock":
                        if computer == "scissor":
                            print("You have won thanks for playing!!")
                        else:
                            print("OOF you lost to the computer thanks for playing anway")

                    elif player3 == "paper":
                        if computer == "rock":
                            print("You have won thanks for playing")
                        else:
                            print("OOF you lost to the computer thanks for playing anway")
                
                    elif player3 == "scissor":
                        if computer == "paper":
                            print("You have won thanks for playing")
                        else:
                            print("Oof you lost to the computer thanks for playing any way.")

                    else:
                         print("ERROR: You have choose the wrong choice")
                    print()
                    player3 = input("""Do you want to be rock paper or scissors? Or do you want to quit type (quit) to end game (Type in your choices in lowercase): """)
                    
                    
                
            if gamer == secret2:
                print("Starting the decoding and encoding game")
                time.sleep(2)
                message = input("Enter a message to encode or decode: ") 
                message = message.upper()
                output = ""
                for letter in message:
                    if letter.isupper():
                         value = ord(letter) + 13
                         letter = chr(value)
                         if not letter.isupper():
                            value -=26
                            letter = chr(value)
                output +=letter
    
                print("This is your decoded/encoded message:", output) 
                time.sleep(2)

                print("Thankyou for playing the Decoding and encoding game")


              

            
            if gamer == secret3:
                print("Starting Guessing game please wait while we set it up.")
                time.sleep(4)
                print("Importing game...  Getting game setup")
                time.sleep(4)
                print("Gaming Starting...")
                time.sleep(1)
                import guessingGame
                
                
                
          
            
            
            
            
            
            
            
            
            
            
            
            if gamer == secret4:
                print("Starting Random Password generator please wait while we set it up")
                time.sleep(4)
                print("Importing game...  Getting game setup")
                time.sleep(4)
                print("Gaming Starting...")
                time.sleep(1)
                import password
                print("Your passwords are displayed above!" )
                print("Thank you for playing Random password generator.")


            if gamer == secret5:
                print("Starting Magic 8 ball game please wait.")
                time.sleep(3)
                print("Importing Game... Setting up game")
                time.sleep(3)
                print("Game starting")
                time.sleep(1)
                import magic8Ball
        

                









           
        if game2 == secretWord4:
                print("Okay bye you wasted your time unlocking this if you didnt want to play lol")
   
        else:
            print("You have been kicked out of the game Incorrect pin / response to question or you have quit the game thanks for playing.")
                
    
                 
    

   
        



if player == secretWord2:
    print("Enjoy the rest of your day.")




 

            


         
    

       
        