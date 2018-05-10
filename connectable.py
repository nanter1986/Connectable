import random

def noticeSomething():
    notices=["why now?",
            "why here?",
            "why this?"]
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
    options=["when","where","how"]
    choice=random.choice(options)
    x=["activity","need","work","hobby"]
    randomX=random.choice(x)
    reaction=["pleasure","dislike","surprise","sadness"]
    randomReaction=random.choice(reaction)
    print("i did "+randomX+" and someone reacted with "+randomReaction)
    print(choice+" do you do "+randomX+"?")

greeting()
shareSomething()

