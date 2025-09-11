# Nang's Introduction 
import time     #time function
import sys       # system library

def slow_print(text, delay=0.05):  #typing effect
    for char in text:
        sys.stdout.write(char)     #write one char
        sys.stdout.flush()         #show immed
        time.sleep(delay)          #pause b4 showing the next char
    print()

slow_print(" Hello, welcome to my GitHub!")
slow_print("I'm Nang Eaindra Hein ")
slow_print("A Computing Science graduate & Web Developer ")
slow_print("Skills: Python  | JavaScript | React | Node.js  | MongoDB ")
slow_print("Multilingual: English  | Thai | Burmese ")
slow_print("Passionate about building apps that make learning fun and easy ")

slow_print("\nThanks for visiting my profile! ")

