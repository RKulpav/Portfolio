#[Libraries]
from microbit import *

#[Global variables]
count1 = 0
count2 = 0
stage = 1

option = 1

#[Functions]
def add(num1, num2):
    result = num1 + num2
    
    if result > 10:
        display.scroll(str(result), delay = 130, loop = True)
    else:
        display.show(str(result))

def subtract(num1, num2):
    result = num1 - num2
    
    if result < 0:
        display.scroll(str(result), delay = 130, loop = True)
    else:
        display.show(str(result))

#[Main]
display.scroll("+ OR -", delay = 90, wait = True)

display.show(Image(
                    "00000:"
                    "00900:"
                    "09990:"
                    "00900:"
                    "00000"
))
option = 1

while stage < 4:
    #Stage 1; get the operation
    if button_a.was_pressed() and stage == 1:
        #Switches between the two options: addition and subtraction
        if option == 1: #Addition
            option = 0 #Change option to subtraction
            display.show(Image(
                "00000:"
                "00000:"
                "09990:"
                "00000:"
                "00000"
            ))
        elif option == 0: #Subtraction
            option = 1 #Change option to addition
            display.show(Image(
                "00000:"
                "00900:"
                "09990:"
                "00900:"
                "00000"
            ))
    elif button_b.was_pressed() and stage == 1: #Locks in the operation that will be used
        stage = 2
        display.scroll("NUMBER 1", delay = 90, wait = True)
        display.show("0")
    
    #Stage 2; get the first number
    if button_a.was_pressed() and count1 <= 8 and stage == 2:
        count1 = count1 + 1
        display.show(str(count1))
    elif button_b.was_pressed() and stage == 2: #Locks in the first number
        stage = 3
        display.scroll("NUMBER 2", delay = 90, wait = True)
        display.show("0")

    #Stage 3; get the second number
    if button_a.was_pressed() and count2 <= 8 and stage == 3:
        count2 = count2 + 1
        display.show(str(count2))
    elif button_b.was_pressed() and stage == 3: #Locks in the second number
        stage = 4 #Breaks the loop
        display.scroll("RESULT", delay = 90, wait = True)

#Adds/subtracts the two numbers and displays it
if option == 1: #Addition
    add(count1, count2)
else: #Subraction
    subtract(count1, count2)
