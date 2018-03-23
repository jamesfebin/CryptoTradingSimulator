import time
import sys

def dramaticTyping(string):
    for char in string:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.10)
