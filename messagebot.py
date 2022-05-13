import time
import pyautogui as spambot
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
    f.close()
    for line in messages:
        kb.type(line)
        spambot.press("enter")
        time.sleep(0.5)   

if __name__ == "__main__":
    time.sleep(5)
    if len(sys.argv) > 1:
        if sys.argv[1] == 'fr':
            write('french_jokes')
        elif sys.argv[1] == 'eng':
            write('eng_jokes')
        elif sys.argv[1] == 'common':
            write('common_messages')
        elif sys.argv[1] == 'all':
            write('eng_jokes')
            write('common_messages')
            write('french_jokes')
    else:
        write('eng_jokes')
        write('common_messages')
        write('french_jokes')
