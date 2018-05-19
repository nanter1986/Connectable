import random

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
    elif liking=="3":
        likeFelling="0k"
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
    return who
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
    return time

def reactionMethodToAsk():
    subject=getSubject()
    likeFeeling=getLikeFeeling()
    who=getWho()
    time=getTheTime()
    if time=="1":
        print("{} {} {}".format(who,likeFelling,subject))
        print("how do you feel about {}?".format(subject))
    elif time=="2":
        print("{} will probably {} {}".format(who,likeFeeling,subject))
        print("how do you feel about {}?".format(subject))

def noticeGreeting():
    print("what positive did you notice?\n")
    observation=input("enter positive observation")
    opposite=input("enter opposite of observation")
    joke=input("0.serious\n1.joke")
    if joke=="1":
        print("you are excellent at {}".format(opposite))
    else:
       print("you are good at {}".format(observation)) 

def startOptions():
    print("what do you want to do?")
    print('''1.discuss subject
        2.greeting with notice
    ''')
    choice=input("please choose\n")
    if choice=="1":
        reactionMethodToAsk()
    elif choice=="2":
        noticeGreeting()
    else:
        print("incorrect input")
        startOptions()

startOptions()
