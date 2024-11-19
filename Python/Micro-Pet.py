#[Modules]
from microbit import *
from time import sleep

#[Global variables]
happiness = 100 #How happy the pet is

#[Functions]
#Pet emotions
def happy():
    return display.show(Image(
        "05050:"
        "05050:"
        "00000:"
        "50005:"
        "05550"
    ))

def upset():
    return display.show(Image(
        "05050:"
        "05050:"
        "00000:"
        "55555:"
        "00000"
    ))

def depressed():
    return display.show(Image(
        "05050:"
        "05050:"
        "00000:"
        "05550:"
        "50005"
    ))

#Decrease the pet's happiness every second
def happinessDecrease():
    global happiness
    if happiness > 0:
        happiness = happiness - 2
        sleep(1)

#Sets the pet's emotion to the current level of happiness
def setEmotion():
    #Used to determine which emotion to display
    if happiness > 80:
        happy()
    elif happiness < 80 and happiness > 30:
        upset()
    elif happiness < 30:
        depressed()

#[Main]
while True:
    setEmotion()
    
    if button_a.was_pressed(): #Give treat to pet; increases happiness
        if happiness < 93: #Pet cannot have above 100 happiness!
            happiness = happiness + 8
            setEmotion()
    elif button_b.was_pressed(): #Display current happiness level
        display.scroll(str(happiness), delay = 100, loop = False, wait = True)
        setEmotion()

    happinessDecrease()
