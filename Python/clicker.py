from time import sleep
import mouse
import keyboard

while True:
    print("Click!")
    mouse.click()
    sleep(0.01)

    if keyboard.is_pressed('q'):
        break