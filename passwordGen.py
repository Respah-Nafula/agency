# Import random
from random import random
import string
print("hello welcome to password generator")
length = int(input("enter the length of the password: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
print(lower)
print(upper)
num = string.digits
symbols=string.punctuation
all = lower + upper + num + symbols
temporary=random.sample(all,length)
print(temporary)
password = "".join(temporary)
print(password)