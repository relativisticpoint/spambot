import time
import pyautogui as auto
from pynput import *
import random
import codecs

def write():
    counter=0
    f = open('./jokes.txt','r',encoding='utf-8')
    #Other way of writing the sentences using a simulated keyboard input to handle unicode characters
    kb = keyboard.Controller()
    messages = f.readlines()
    for line in messages:
        
        kb.type(line)
        auto.press("enter")
        time.sleep(0.5)   
    print(counter)

if __name__ == "__main__":
    time.sleep(5)
    write()
