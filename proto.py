# Prototype for my game
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)

delay_print("hello world\n")

text = input()

delay_print(text+"\n")
