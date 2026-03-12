# Program 21: Invoke Function After Specific Time

import time
import math

def delayed():
    print("Square root after specific milliseconds:")
    print(math.sqrt(16))
    print(math.sqrt(100))
    print(math.sqrt(25100))

time.sleep(2)   # 2 seconds delay
delayed()