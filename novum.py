# Prototype for interactive fiction.
import time
import sys
import climage

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    print() #Without this print statement, the delayprint doesn't make a new line. 

def word_print(s):
    for word in s.split():
        time.sleep(0.1)
        for c in word:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.06)
        print(" ",end="")
    print() #Without this print statement, the delayprint doesn't make a new line.
#delay_print("hello world\n")

def img_print(name):
    out = climage.convert("../images/{}".format(name),width=50)
    print(out)

#text = input()

#print("Blah blah \033[0;32mthis part will be green\033[00m blah blah.")

#print("Blah blah \033[0;31mthis part will be red\033[00m blah blah.")
#delay_print(text+"\n")
"""
# Test colored text:
for i in range(108):
    print("\033[0;{}mWhat color does this print as?\033[00m".format(i))

for i in range(10):
    for j in range(10):
        print("\033[0;{};{}mThe Lazy Brown Dog Jumps Over The Silly Goose\033[00m".format(30+i,40+j))
"""
# My formatted print function takes the character and text and prints it as.
def fpri(ctr,txt):
    # dictionary of character names and 
    ctrdict = {"ben":"33","HAL":"31","-->":"03","Dave":"32","Frank":"34","4NGEL":"33","Rozen":"32","Uric":"34","Faerri":"31","Nemo":"31","5ERAPH":"37"}
    # list of characters that get slow printing.
    slow = ["HAL","4NGEL","5ERAPH","-->"]
    # formatted text to be written:
    if ctr in slow:
        outtxt = "\033[0;01;03m{}: \033[00m\033[0;{}m{}\033[00m".format(ctr,ctrdict[ctr],txt.upper())
        delay_print(outtxt)
    else:
        #time.sleep(1.3)
        outtxt = "\033[0;01;03m{}: \033[00m\033[0;{}m{}\033[00m".format(ctr,ctrdict[ctr],txt)
        delay_print(outtxt)

# Formatting function for list of choices
def choice(lst):
    for (ind,cho) in enumerate(lst):
        print("{}: {}".format(ind+1, cho))
    intxt = input()
    while True: 
        try:
            if int(intxt) <= len(lst) and 1 <= int(intxt):
                return lst[int(intxt)-1]
            else:
                intxt = input()
        except ValueError:
            intxt = input()

# Formatting function for list of choices with a numeric output.
# [list of string choices] -> [return string, index]
def fcho(lst):
    for (ind,cho) in enumerate(lst):
        print("{}: {}".format(ind+1, cho))
    intxt = input()
    while True: 
        try:
            if int(intxt) <= len(lst) and 1 <= int(intxt):
                return [lst[int(intxt)-1],int(intxt)]                                                                                                                       
            else:
                intxt = input()
        except ValueError:
            intxt = input()

#Want to clean of the interface so that the choices aren't shown after they're made.
# Test Scene with different options!
# void -> Int
def c1():
    fpri("Dave","Hey Frank, what time is it?")
    fpri("Frank","I don't know, what have you had for dinner recently?")
    data = fcho(["corn","regular bat","corporate bats"])
    fpri("Dave",data[0])
    return data[1]

def c21():
    fpri("HAL","CORN?")
    fpri("Dave","Yes that's all")
    fpri("Frank","I think that is enough")
    data = fcho(["It was","It was not"])
    fpri("Dave",data[0])
    return data[1]


def c22():
    fpri("HAL","REGULAR BAT?")
    fpri("Dave","Yes that's all")
    fpri("Frank","I think that is enough")
    data = fcho(["It was","It was not"])
    fpri("Dave",data[0])
    return data[1]


def c23():
    fpri("HAL","CORPORATE BATS?!?!?!?")
    fpri("Dave","Yes that's all")
    fpri("Frank","I think that is enough")
    data = fcho(["It was","It was not"])
    fpri("Dave",data[0])
    return data[1]
def e1():
    fpri("HAL","You chose ending 1")

def e2():
    fpri("HAL","You chose ending 2")
"""
Here's how this works.
1. You make the dialogue leading up to a decision in a choice function and return the option that was selected.
2. Put them in a tree (nested list) 

TODO: 
- State update?
- Scenes that don't have any choices.
"""

def s1():
    choices = [c1,[c21,[e1],[e2]],[c22,[e1],[e2]],[c23,[e1],[e2]]]
    while len(choices) != 1:
        data = choices[0]() 
        choices = choices[data]
    choices[0]()
#Test Scene
def hal_scene():
    img_print("jup2.jpg")
    fpri("HAL","I hope the two of you are not concerned about this.")
    fpri("Dave",choice(["No, I'm not HAL.","Yes, I am HAL.","*silence*"]))
    fpri("HAL","Are you quite sure?")
    fpri("Dave",choice(["HAL, I'm having second thoughts","Yeah. I'd like to ask you a question, though."]))
    fpri("HAL","Of course.")
    fpri("Dave",choice(["How certain are you about the accuracy of the other 9000 series computer?","Are there any other concerns with the operation of the ship?","How would you account for this discrepancy between you and the twin 9000?"]))
    fpri("HAL","Well, I don't think there is any question about it. It can only be attributable to human error. This sort of thing has cropped up before, and it has always been due to human error.")
    fpri("Frank","Listen HAL. There has never been any instance at all of a computer error occurring in the 9000 series, has there?")
    fpri("HAL","None whatsoever, Frank. The 9000 series has a perfect operational record.")
    fpri("Frank","Well of course I know all the wonderful achievements of the 9000 series, but, uh, are you certain there has never been any case of even the most insignificant computer error?")
    fpri("HAL","None whatsoever, Frank. Quite honestly, I wouldn't worry myself about that.")
    fpri("Dave",choice(["Well, I'm sure you're right, HAL. Uhm, fine, thanks very much.","HAL, I'm going to need to shut you down temporarily","*shuts down HAL*"]))
    img_print("hal.jpg")
    return
"""
for x in range (0,5):  
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(0.5)
#Image test
print(output)
print(output2)
"""
# Demo for the HAL scene.
#hal_scene()

#---------------------- INTERROGATION -------------------------o

## This is going to get modified.
state = []
# Example!
def c1():
    fpri("Dave","Hey Frank, what time is it?")
    fpri("Frank","I don't know, what have you had for dinner recently?")
    data = fcho(["corn","regular bat","corporate bats"])
    fpri("Dave",data[0])
    return data[1]
def intc1():
    fpri("Nemo","Captain Rozen, welcome to my office. I hope that you found the journey here an enjoyable one.")
    data = fcho(["You certainly seem to have a firm control over your servants.","An elevator ride past an aquarium full of whale-bat-spider chimeras seems a little gaudy for a corporation doesn't it?","I found the decoration to be to my liking.","You certainly seem to have a flair of... some sort."])
    fpri("Rozen",data[0])
    fpri("Nemo",["Nonsense, the Travenents are not servants and they do as they please. They have been programmed with the companies interests in mind though.","Nonsense. Kerensky Productions must maintain its image. How better to do that then with a display of our prowess in manipulating biology. Besides, does it not please you to see creatures from your home planet improved on?","Ah, but I can sense your insincerity. I can never understand why humans begin their interactions with such hesitance.","Aha! I'm glad you noticed. I love my theatrics. The scenery helps boost the morale of the company. We're still trying to work on rectifying that awful smell, but hopefully it does not offend you."][data[1]-1])
    fpri("5ERAPH","Nemo, this meeting is a matter of business, not of pleasantry. Why not present our proposal to 4NGEL and Captain Rozen?")
    fpri("Nemo","You must forgive 5ERAPH's interruption. It seems that he was not programmed to be a good host. Nevertheless, we may as well get down to business.")
    return
def testscene():
    choices = [c1,[c21,[e1],[e2]],[c22,[e1],[e2]],[c23,[e1],[e2]]]
    while len(choices) != 1:
        data = choices[0]()
        choices = choices[data]
    choices[0]()

# A function to run any scene... Here choices is a list of lists of functions.
def runscene(choices):
    #choices = [c1,[c21,[e1],[e2]],[c22,[e1],[e2]],[c23,[e1],[e2]]]
    while len(choices) != 1:
        data = choices[0]()
        choices = choices[data]
    choices[0]()

interrogation_scene = [intc1]
runscene(interrogation_scene)

