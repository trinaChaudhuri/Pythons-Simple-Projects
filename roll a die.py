import random
for x in range(1):
    print(random.randrange(1,6))
print("do you want to roll die again")
choice=input()
if choice=="yes":
    for x in range(1):
        print(random.randrange(1,6))

