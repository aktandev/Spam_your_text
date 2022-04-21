import time

import pyautogui

msg = input("Enter the message: ")
n = input("How many times?: ")

count = 5
while count != 0:
    print(f"{count} seconds to start")
    time.sleep(1)
    count -= 1

print("Spam has end!!!")

for i in range(0, int(n)):
    pyautogui.typewrite(msg + "\n")
