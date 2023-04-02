# Prototype for interactive fiction.
import time
import sys
import climage

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        #Playing Speed
        #time.sleep(0.04)
        #Testing Speed
        time.sleep(0.01)
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
    fpri("  HAL","I hope the two of you are not concerned about this.")
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
    fpri("Rozen","Yes. Remote system centered around a capital planet called Noblaris. Steady supply of minerals and water. Mostly planets owned by Albacorp.")
    fpri("Nemo","That last feature of Noblar is quite regrettable. Based on Albacorp's recent increase in Macrochip production it seems that they must have discovered quite a trove of Fermi-ferrides. A Kerensky Productions spy. I mean... employee was able to trace the source of the ore to Albacorps holdings in the Noblar system.")
    fpri("Rozen","You want us to get you a hold full or Fermi-ferrides.")
    fpri("Nemo","We're ready to pay five megakernels per kilogram.")
    data1 = fcho(["At that rate it sounds like there's gotta be a catch.","We'll see what we can do.","What, is this your dog's ore that they took or something? That price makes it seem awfully personal."])
    fpri("Rozen",data1[0])
    fpri("Nemo",(["A catch? The complications of the mission would be left to you and your crew of course.","Very well.","You could say it's personal. It is of great importance that the ore is secured."][data1[1]-1]+" There's also one more thing. It would be in Kerensky Productions interest if Albacorp's mining venture was delayed. Perhaps some of their machines break down, perhaps some of their workforce mysteriously vanishes. I'll leave the specifics to you."))
    fpri("Rozen","I'm a theif not a demolitionist. I'm not going to run a sabotage mission for you.")
    fpri("Nemo","A shame. Nontheless your services will be of great value. Does the pay please you?")
    data2 = fcho(["For a mission like that we'd need twice as many kernels.","I want a prototype and first access to whatever you're building with the Fermi-ferrides as extra compensation though.","Someone like me can always use a corporation on their side. If we get you this ore, I'll expect to be able to call in a favour down the line."])
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
    fpri("-->","THREE DAYS LATER. The scent of dark roast koff fills Alterity's bridge.")
    fpri("Rozen","Uric, any updates on the location of the ore?")
    fpri("Uric","Based on fuel shipments to the Noblar system it seems like they're digging on Ashera IV. They've also recently relocated a significant portion of their Noblarian population there.")
    fpri("Rozen","Security report?")
    fpri("Uric","Michelson detection for incoming spacecraft, grounded missiles and a small fleet of combat-ready starships. Nothing we haven't dealt with before, but not an easy mission.")
    fpri("Faerri","I have a contact on Noblaris. They say that Albacorp has been experimenting with bioengineered guards.")
    fpri("4NGEL","Albacorp also employs an array of drones and has a network of laser-powered detectors. Alterity's claoking system will likely shield us from the drones, but the lasers will still detect us.")
    data1 = fcho(["Let's get through the Michelson detectors by using the same trick as on Kazi. We'll switch the main engines from sulphentine to blacktar while we're in detection range.","Let's go in through the front. Forge papers and a story and we'll come in through customs."])
    fpri("Rozen", data1[0] + " Faerri, what can you tell me about Albacorp mines?")
    fpri("Faerri","They have a standardized operation across their Noblar planets. They run bots for extraction, then take the raw ore to a refinery before shipping it off to Noblaris to be put into production.")
    fpri("Rozen","How do they move the ore?")
    fpri("Faerri","They use a magnetorail to get it to the refinery and then a hulk of a starcruiser to ship it to Noblaris.")
    fpri("Rozen","4NGEL, how realistic do you think it would be to intercept the starcruiser?")
    fpri("4NGEL","According to intergalactic records, their only large vessels in this system are a class EK-417 Hipparchus and a Halberd 60. Both of which are much better equipped for assault than us. Both are likely to have a much bigger and more heavily armed crew than we could stand to face.")
    fpri("Rozen","I would rather not have a repeat of what happened last time we tried to sneak onto a cruiser unnoticed. We'll do a raid on their magnetorail.")
    fpri("Faerri","We could stop the magnetorail with a modified EMP.")
    fpri("Uric","We'd also have to account for shileding on the generators.")
    
    global state
    state["method"] = ["blacktar","security papers"][data1[1]-1]
    fpri("Rozen","We wont be able to keep the train down for very long. They'll also probably send out someone to investigate once the signal from the train stops. It'll have to be a 'smash and grab'.")
    fpri("Uric","That's my favorite kind of heist.")
    fpri("Faerri","I prefer a little more subtlety, but this should be fun.")
   # fpri("Rozen","Let's have some fun. 4NGEL, what are the odds we succeed?")
    #fpri("4NGEL","With the given data I rate our odds of leaving with the ore 91.55%. Odds of successfully sabotaging the mining rig and retrieving the ore are lower at 82.14%")
    fpri("Rozen","Alright. Uric, get the {}, and see if you can find the magnetorail route. I want all hardware inspected prior to departure. Faerri, get us an EMP, a goat and get Alterity ready for action. 4NGEL and I are going to see if we can do anything about the lasers. It wouldn't be great to have bioengineered monsters on our tail before we get to the magnetorail. Everyone go get a good night's sleep.".format(state["method"]))
    fpri("Uric","You know that githarians don't need to sleep right?")
    fpri("4NGEL","Neither, technically, do I. Although the sentiment is appreciated.")
    fpri("Faerri","I will have a good sleep thank you. Although centrians sleep, we do not dream. I always thought that it would be enjoyable to have dreams.")
    return 1 

def on_planetc3():
    img_print("onworld.gif")
    fpri("-->","The tundra of green dust was silent for now.")
    fpri("Rozen","4NGEL, how long until we get to the interception point?")
    fpri("4NGEL","Approximately 1.34 times ten to the forty-seven Plank times.")
    fpri("Rozen","In earth units?")
    fpri("4NGEL","Around two earth hours.")
    fpri("Faerri","There's something coming up on sonar. Two things actually. Looks like there's a storm directly ahead. We can track around it in either direction, but if we change our course to south-west we'll run into a massive object. The object is emitting more radiation than the ground, but not dangerous levels.")
    fpri("Uric","Either new course would still leave us with enough time before the magnetorail arrives.")
    data1 = fcho(["Let's keep going west. I'm sure Alterity can handle the storms on this planet.","Let's go southwest. I want to check out that object.","Let's go northwest. I don't want to run into anything unexpected."])
    fpri("4NGEL","Plotting route {}".format(["through storm.","southwest.","northwest."][data1[1]-1]))
    global state
    state["path"] = ["Storm","Ship","Swamp"][data[1]-1]
    return data1[1]

def westc41():
    img_print("lightning.jpg")
    fpri("-->","Just like storms on earth, storms on Ashera IV come with lightning. Unlike storms on earth, storms on Ashera IV have winds of up to 13 kilaklicks (that's 400 kilometers per hour for those who prefer earth units.)")
    fpri("Rozen","AHHHHHHHHHHHH!!!")
    fpri("Uric","ARRRRRROOOOOOOOOOOOOOO!!!")
    fpri("Faerri","UNNNNNNNNNNNNNNNG!!!")
    fpri("4NGEL","What is the saying on earth? When in Rome?")
    fpri("4NGEL","... Here goes nothing.")
    fpri("4NGEL","@&#$%&@#$&%&@#%$@#@%#$&%@&#%$!!!")
    fpri("-->","ONE HOUR LATER.")
    fpri("Rozen","Status report.")
    fpri("4NGEL","Cloaking is damaged, but functional. Emag shields are at 40%, but we're regenerating them.")
    fpri("Uric","Engines look good to me.")
    fpri("Faerri","Kinematic power supply is at 99%. Looks like all that blowing around was good for something.")
    fpri("Rozen","Looks like the voltcannon also managed to pickup a lot of static electricity. If we face any complications they'll be in for quite the surprise.")
    return 1

def westc42():
    img_print("ship.jpg")
    fpri("-->","Craters in the green desert whisper bygone conflict.")
    fpri("Faerri","We're approaching the object now.")
    fpri("Uric","I'm going to go make some more koff. Anyone want some?")
    fpri("Rozen","No thanks. I'm curious about this thing.")
    fpri("4NGEL","Yes please.")
    fpri("4NGEL","... I am trying to introduce humor into my default protocol. Did I do a good job.")
    fpri("Rozen","You did great 4NGEL. Faerri, what are we seeing?")
    fpri("Faerri","It's a downed starship. Looks like an AX17 Democritus. Not too different from our own Alterity here.")
    fpri("Rozen","4NGEL, see if any of their communications are live.")
    fpri("4NGEL","There's a signal, but it's static.")
    fpri("Uric","This is good koff. We have time to go down and check it out.")
    fpri("Rozen","Let's see what there is to see then.")
    img_print("qc.jpg")
    fpri("-->","The crew had never seen animals living quite so happily as the ones that lived in Swordbreaker, an AX17 Democritus model starcraft.")
    fpri("Uric","Do you have creatures like these back on earth?")
    fpri("Rozen","We have something like them. They're called squirrels or chipmunks. They're a little smaller than these guys though.")
    fpri("Uric","Looks like this ship went down in a firefight.")
    fpri("Rozen","Hopefully we avoid whatever happened to Swordbreaker")
    fpri("Uric","Most of the systems are too damaged to use, but there are a few parts I can salvage.")
    fpri("Rozen","Fill your boots. I'm going to look for the black box.")
    fpri("-->","SEVERAL MINUTES LATER.")
    fpri("Rozen","You want the good news or the bad news?")
    fpri("Faerri","Bad news.")
    fpri("Rozen","No black box. Looks like someone already did the archeology on this thing.")
    fpri("Uric","Good news is that Swordbreaker had some salvagable parts. Not to mention a live photonic missile.")
    fpri("Rozen","Alright. Let's get back on course.")
    return 1

def westc43():
    img_print("swamp.jpg")
    fpri("-->","Eventually, the dusty green desert gave way to an ocean of sorts.")
    fpri("Rozen","Well this is certainly interesting.")
    fpri("Uric","Unsettling might be a better word.")
    fpri("Faerri","I think their beautiful.")
    fpri("4NGEL","Their proportions suggest that they've been genetically engineered.")
    fpri("Rozen","The tentacles are not really my style, but it's better than what Kerensky was cooking up.")
    fpri("Uric","I think that one just ate it's friend.")
    fpri("Rozen","Maybe I spoke too soon.")
    fpri("Faerri","I still like them.")
    fpri("Uric","They're literally swimming death machines. Tentacles, stingers, teeth, a beak. I think I just saw one discharge electricity.")
    fpri("4NGEL","Perhaps Albacorp is seeing how these creatures fare in a natural environment.")
    fpri("Rozen","I'm just glad we're in the air. I wonder what use these could possibly have.")
    return 1

def rail5():
    img_print("tressel.jpg")
    fpri("-->","The dusty green desert is broken by long metallic strips. The rails reminded Rozen of ancient musical notation.")
    fpri("Faerri","Here we are.")
    fpri("Rozen","Remeber the plan. When the magnetorail comes, we'll fire the EMP. The EMP has been calibrated to kill the train, but still leave 4NGEL and our engines up. Then once the train has stopped we'll get on the ground. Uric and I will head out and attach these cables to the end of a car containing fermi-ferrides. Then we'll run back to the ship and ride off into the sunset while the cables pull the cargo up into our hold.")
    fpri("Uric","30 minutes until the magnetorail gets here.")
    fpri("-->","90 MINUTES LATER.")
    fpri("Rozen","Why aren't they here yet?")
    fpri("Uric","They should be here now.")
    fpri("4NGEL","Here they come. I can sense the change in the electric field.")
    fpri("Rozen","Showtime. Activate the EMP in 5.")
    fpri("Rozen","4.")
    fpri("Rozen","3.")
    fpri("Rozen","2.")
    fpri("Rozen","1.")
    fpri("4NGEL","Activating the EMP.")
    fpri("Faerri","Why didn't the train stop?")
    fpri("4NGEL","It seems that they've shielded their systems.")
    fpri("")
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

# A function that can run scenes in any order
def secondary_runscene(scenes):
    data = scenes[0]()
    while data < len(scenes):
        data = scenes[data]()
    return

interrogation_scene = [intc1,[reportc2]]
#uncomment this to run the whole game
#runscene(interrogation_scene)
#Testing a particular scene below:
# intc1()
reportc2()
