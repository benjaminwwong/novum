# Prototype for interactive fiction.
import time
import sys
import climage

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.06)
    print() #Without this print statement, the delayprint doesn't make a new line. 

#delay_print("hello world\n")

def img_print(name):
    out = climage.convert("../images/{}".format(name),width=50)
    print(out)

#text = input()

#print("Blah blah \033[0;32mthis part will be green\033[00m blah blah.")

#print("Blah blah \033[0;31mthis part will be red\033[00m blah blah.")
#delay_print(text+"\n")

# Test colored text:
#for i in range(108):
#    print("\033[0;{}mWhat color does this print as?\033[00m".format(i))

# My formatted print function takes the character and text and prints it as.
def fpri(ctr,txt):
    # dictionary of character names and 
    ctrdict = {"ben":"33","HAL":"31","Dave":"32","Frank":"34"}
    # list of characters that get slow printing.
    slow = ["HAL"]
    # formatted text to be written:
    outtxt = "\033[0;01;03m{}: \033[00m\033[0;{}m{}\033[00m".format(ctr,ctrdict[ctr],txt)
    if ctr in slow:
        delay_print(outtxt)
    else:
        time.sleep(1.3)
        print(outtxt)
"""
fpri("ben","how are you today?")
fpri("HAL","DAISY, DAISY")
fpri("Frank","Hello squireels")
fpri("Dave","I want a boat")
output = climage.convert("world2.gif",width=40)
output2 = climage.convert("worldgen.gif",width=40)
"""
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

#Want to clean of the interface so that the choices aren't shown after they're made.

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
hal_scene()
