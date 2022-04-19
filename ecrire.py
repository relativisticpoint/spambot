import time
import pyautogui as auto
from pynput import *
import random
import codecs
import sys
def write(fichier):
    fichier = './'+fichier+'.txt'
    f = open(fichier,'r',encoding='utf-8')
    #Other way of writing the sentences using a simulated keyboard input to handle unicode characters
    kb = keyboard.Controller()
    messages = f.readlines()
    for line in messages:
        
        kb.type(line)
        auto.press("enter")
        time.sleep(0.5)   

if __name__ == "__main__":
    time.sleep(5)
    if len(sys.argv) > 1:
        if sys.argv[1] == "fr":
            write('jokes')
        elif sys.argv[1] == "eng":
            write('common')
        elif sys.argv[1] == "all":
            write('common')
            write('jokes')
    else:
        write('common')
        write('jokes')
