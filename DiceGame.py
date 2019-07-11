import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
total = dice1 + dice2 + dice3
print("What is your name?")
name = input(">")
print("Hello, "+ name +"!")
print("Rolling the dice...")
print("Die 1: "+ str(dice1))
print("Die 2: "+ str(dice2))
print("Die 3: "+ str(dice3))
print("Total value: "+ str(total))
if total <= 9:
  print(name +" lost")
else:
  print(name +" won")

