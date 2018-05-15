import random

def blamedFor():
    print("blamedFor################")
    print("Are you being blamed?")
    choice=input("choose\n1.yes\n2.no")
    if choice=="1":
        blameSolution()
    elif choice=="2":
        greeting()
    else:
        print("incorrect input")
        blamedFor()

def blameSoft():
    print("blameSoft################")
    options=["how","when","where"]
    choice=random.choice(options)
    print(choice+" should I do it")
    greeting()

def blameHard():
    print("blameHard################")
    options=["how","when","where"]
    choice=random.choice(options)
    print("Im sorry this happened.I accept my mistake and respondibilities")
    print(choice+" should I do it?")
    greeting()

def blameSolution():
    print("blameSolution################")
    print("how strongly are you being blamed?")
    choice=input("1.hard\n2.soft")
    if choice=="1":
        blameHard()
    elif choice=="2":
        blameSoft()
    else:
        print("incorrect input")
        blameSolution()

def noticeSomething():
    print("noticeSomething################")
    notices=["why now?",
            "why here?",
            "why this?",
            "what does it look like?what if this was true?"]
    return random.choice(notices)

def greeting():
    print("greeting################")
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
    print("shareSomething################")
    #story should have at least action and reaction
    options=["when","where","how"]
    choice=random.choice(options)
    x=["activity","need","work","hobby"]
    randomX=random.choice(x)
    reaction=["pleasure","dislike","surprise","sadness"]
    randomReaction=random.choice(reaction)
    print("i did "+randomX+" and someone reacted with "+randomReaction)
    print(choice+" do you do "+randomX+"?")

def getSubject():
    subject=input('''choose subject''')
    return subject

def getLikeFeeling():
    likeFelling="ok"
    liking=input('''
                 1.hate
                 2.dislike
                 3.ok
                 4.like
                 5.love
                 ''')
    if liking=="1":
        likeFelling="hated"
    elif liking=="2":
        likeFelling="disliked"
    elif liking=="4":
        likeFelling="liked"
    elif liking=="5":
        likeFelling="loved"
    else:
        print("incorrect input")
        getLikeFeeling()
    return likeFelling

def getWho():
    who=input('''who?
              ''')
def getTheTime():
    time=input('''choose time
               1.past
               2.future
               ''')
    if time=="1" or time=="2":
        pass
    else:
        print("incorrect input,try again")
        getTheTime()

def reactionMethodTAsk():
    subject=getSubject()
    likeFeeling=getLikeFeeling()
    who=getWho()
    time=getTheTime()
    if time=="1":
        print(who+" "+likeFelling+" "+subject)
        print("how do you feel about "+subject+"?")
    elif time="2":
        print(who+" will probably "+likeFelling+" "+subject)
        print("how do you feel about "+subject+"?")

reactionMethodToAsk()
