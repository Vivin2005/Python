
import random

upper_case=("QERTYUIOPASDFGHJKLMNBVCXZ")

lower_case=("qwertyuioplkjhgfdsazxcvbnm")

num=("1234567890")

sym=("@#$&+/?!;:*")

all=upper_case+lower_case+num+sym

length=int(input("ENTER THE LENGTH OF THE PASSWORD YOU WANT:"))

password="".join(random.sample(all,length))

print(password)