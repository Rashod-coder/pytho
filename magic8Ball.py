import random
import time
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable", "Positive","Never ever happening not a single chance", "I dont think so", "I think so", "Yep 100% positive", "Nope you wont", "HAHAHAHAHA in your dreams"]

## Following function asks user question, then returns random results from responses
print("Welcome to zee Magic 8 ball ask questions about yourself or other enjoy playing.")
time.sleep(5)

def answerQuery():
    question = input("Ask a question from the magic 8 ball and you shall recive a response good luck:  ")
    print("Let me think Hmmmm... Ooohh what do we have here. Hmmmm... Hmmmm I see Ah this is what IM looking for.")
    time.sleep(2)
    print("Ah here we go ")
    time.sleep(2)
    print(random.choice(responses))
    print("\n")
answerQuery()
time.sleep(3)
print("Thank you for playing!!!!!")

secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
while secondQuestion == str("Y"):
    answerQuery()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
else:
    print(input("Press any key to exit"))

    print("Thanks you for playing Magic 8 ball")