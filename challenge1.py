import math
import netrc
import os
import random
import re
import sys 



n= int(input("enter a number: "))
n in range(1,100)
if n>100 or n<1:
    print("not applicable! Check the range")
elif n%2==1:
    print("Weird")   
elif n in range(2,5) and n%2==0:
    print("Not Weird")
elif n in range(6,20) and n%2==0:
    print("Weird")
else :
    print("Not Weird")
