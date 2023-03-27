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
    out = climage.convert("images/{}".format(name),width=50)
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
    slow = ["HAL","4NGEL","5ERAPH"]
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

## This is going to get modified by various scenes and the referreced later.
state = {}
# Example!
def c1():
    fpri("Dave","Hey Frank, what time is it?")
    fpri("Frank","I don't know, what have you had for dinner recently?")
    data = fcho(["corn","regular bat","corporate bats"])
    fpri("Dave",data[0])
    return data[1]
def intc1():
    img_print("stars2.jpg")
    fpri("-->","Ozone from the EPR gates below penetrated the 16th story walls of the Kelensky Productions building.")
    fpri("Nemo","Captain Rozen, welcome to my office. I hope that you found the journey here an enjoyable one.")
    data = fcho(["You certainly seem to have a firm control over your servants.","An elevator ride past an aquarium full of whale-bat-spider chimeras seems a little gaudy for a 'professional' doesn't it?","I found the decoration to be to my liking.","You certainly seem to have a flair of... some sort."])
    fpri("Rozen",data[0])
    fpri("Nemo",["Nonsense, the Travenents are not servants and they do as they please. They have been programmed with the companies interests in mind though.","Nonsense. Kerensky Productions must maintain its image. How better to do that then with a display of our prowess in manipulating biology? Besides, does it not please you to see creatures from your home planet improved on?","Ah, but I can sense your insincerity. I can never understand why humans begin their interactions with such hesitance.","Aha! I'm glad you noticed. I love my theatrics. The scenery helps boost the morale of the company. We're still trying to work on rectifying that awful smell, but hopefully it does not offend you."][data[1]-1])
    #fpri("5ERAPH","Nemo, this meeting is a matter of business, not of pleasantry. Why not present our proposal to Captain Rozen?")
    #fpri("Nemo","You must forgive 5ERAPH's interruption. It seems that he was not programmed to be a good host. Nevertheless, we may as well get down to business. Are you familiar with the Noblar system?")
    fpri("Rozen","...")
    fpri("Nemo","Well. We might as well get down to business. As a Pir-... As a person in your field, I'm sure you're familar with the Noblar system.")
    fpri("Rozen","Yes. Remote system. Steady supply of minerals and water. Mostly planets owned by Albacorp.")
    fpri("Nemo","That last feature of Noblar is quite regrettable. Based on Albacorp's recent increase in Macrochip production it seems that they must have discovered quite a trove of Fermi-ferrides. A Kerensky Productions spy. I mean... employee was able to trace the source of the ore to Albacorps holdings in the Noblar system.")
    fpri("Rozen","You want us to go down there real quiet and come back up with a hold full or Fermi-ferrides.")
    fpri("Nemo","We're ready to pay five megakernels per kilogram.")
    data1 = fcho(["At that rate it sounds like there's gotta be a catch.","We'll see what we can do.","What, is this your dog's ore that they took or something? That price makes it seem awfully personal."])
    fpri("Rozen",data1[0])
    fpri("Nemo",(["A catch? The complications of the mission would be left to you and your crew of course.","Very well.","You could say it's personal. It is of great importance that the ore is secured."][data1[1]-1]+" There's also one more thing. It would be in Kerensky Productions interest if Albacorp's mining venture was delayed. Perhaps some of their machines break down, perhaps some of their workforce mysteriously vanishes. I'll leave the specifics to you."))
    data2 = fcho(["For a mission like that we'd need twice as many kernels.","I can make sure their mines run a little slower after we're through. I want a prototype and first access to whatever you're building with the Fermi-ferrides as extra compensation though.","Someone like me can always use a corporation on their side. If I sabotage Albacorp for you, I'll expect to be able to call in a favour later down the line.","I'm a theif not a demolitionist. I won't run a sabatoge mission for you."])
    fpri("Rozen",data2[0])
    global state
    state["reward"] = ["Money","Technology","Influence","Virtue"][data2[1]-1]
    #img_print("hal.jpg")
    fpri("Nemo","Very well. That can be arranged.")
#    fpri("Rozen","Is there anything else we should know before heading out?")
#    fpri("Nemo","You're dismissed.")
    return 1

# This scene has the party members reporting the findings to captain Rozen. 
def reportc2():
    img_print("spaceship.jpg")
    fpri("-->","THREE DAYS LATER. The scent of dark roast koff fills Alterity's bridge. Nuclear fusion ")
    fpri("Rozen","Uric, what's the ")
    fpri("Uric","")
    fpri("")
    fpri("")
    fpri("Rozen","Let's have some fun. 4NGEL, what are the odds we succeed?")
    fpri("4NGEL","With the given data I rate our odds of leaving with the ore 91.55%. Odds of successfully sabotaging the mining rig and retrieving the ore are lower at 82.14%")
    return 1 
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

interrogation_scene = [intc1,[reportc2]]
#uncomment this to run the whole game
runscene(interrogation_scene)
