import random

def noticeSomething():
    notices=["Did you change that on your appearance?",
            "why on this time?",
            "why here?",
            "why are you doing this?",
            "what are you doing?",
            "why this object?"]
    return random.choice(notices)

def greeting():
    print(noticeSomething())
    print("1.like\n2.have to\n3.nothing better")
    choice=input("Choose please")
    if choice=="1":
        print("why do you like it?")
    elif choice=="2":
        print("why do you have to?")
    elif choice=="3":
        print("what would you like to be doing?")
    else:
        print("incorrect input")
        greeting()

def shareSomething():
    #story should have at least action and reaction

greeting()
