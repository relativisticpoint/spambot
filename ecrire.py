import time
import pyautogui as auto
import random


def write():
    counter=0
    f = open("./common.txt", "r")
    messages = f.readlines()
    f.close()
    for line in messages :
        auto.write(line)
        auto.press("enter")
        time.sleep(0.5)

        
    print(counter)

if __name__ == "__main__":
    time.sleep(3)
    write()
    
