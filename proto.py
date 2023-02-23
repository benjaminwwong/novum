# Prototype for interactive fiction.
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)

delay_print("hello world\n")

text = input()

print("Blah blah \033[0;32mthis part will be green\033[00m blah blah.")

print("Blah blah \033[0;31mthis part will be red\033[00m blah blah.")
delay_print(text+"\n")


