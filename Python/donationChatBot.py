#[Importing modules]
import keyboard
import random
import tkinter
import threading
from time import sleep

#[Creating the window for the control buttons]
window = tkinter.Tk()
window.geometry("250x100")
window.attributes("-alpha", 0.9)
window.configure(bg = "#696969")
window.title("Chat Bot")

#[Random chat messages function]
def randomChatMessages():
    messages = ["Consider supporting me!", "Thank you for any donations!", "Any donations will help towards my goal!", "All donations are appreciated!"]

    randomMessage = random.choice(messages)

    return randomMessage

#[Chat function]
def chat(message):
    #Uses string values to turn it into text and send it into chat

    #[Opening up chat]
    #Sleep is used here because the keyboard module sends inputs very quickly, and often without the sleep, roblox does not detect the input
    keyboard.press("/")
    sleep(0.2)
    keyboard.release("/")

    #[Sending the message into chat]
    messageDelay = 0.2

    keyboard.write(str(message))
    sleep(messageDelay)
    keyboard.send("enter")

#[Jump function]
def jump():
    keyboard.press("spacebar")
    sleep(0.1)
    keyboard.release("spacebar")

#[Emote function]
def emote(emoteNum):
    keyboard.send(".")
    sleep(0.1)
    keyboard.send(str(emoteNum))

#[Main Chat Bot function]
def chatBot():
    global stopBot

    while stopBot == False:
        
        chat(randomChatMessages())
        #The jumping (and emoting) is here because roblox kicks you out if you stay in-game for 20 minutes while afk
        jump()
        sleep(0.5)
        emote(1)
        sleep(40)

#[Main]
#Variable used to stop the bot
stopBot = False

#Starting the bot
def botStart():
    sleep(3) #Small delay, allows the user to minimise bot control menu before the bot starts

    global botThread

    botThread = threading.Thread(target = chatBot)
    botThread.start()

def botStop():
    global stopBot
    stopBot = True

#[Chat Bot start and stop buttons]

buttonStart = tkinter.Button(window, text = "Start", bg = "#2edb3c", width=15, command = botStart)
buttonStart.place(x = 75, y = 15)

buttonStop = tkinter.Button(window, text = "Stop", bg = "#db2e2e", width=15, command = botStop)
buttonStop.place(x = 75, y = 65)

#Creates the window and buttons onto the screen
window.mainloop()
