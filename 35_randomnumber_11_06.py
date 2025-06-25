# Generate a random number and have the user guess it, providing hints such as "too high" or "too low" until they guess correctly.

import random 

while True:
 fix = random.randint(1,9)
 i=1
 while i<=3:
  guess = int(input("guess number:"))
  if fix==guess:
   print("you won the game")
   break
  else:
   if fix > guess:
    print("you guessesd bit big ")
   else:
    print("you guessed bit small")
  i=i+1
 else:
  print("you lost the game")

 ch =str(input("do you want play again(yes/no):"))
 if ch == 'no':
    break
 print ("game over ")
 