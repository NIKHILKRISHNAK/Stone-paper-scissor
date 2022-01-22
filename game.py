print("="*78)
print("\n")
print("STONE-PAPER-SCISSOR")
print("\n")
print("Enter your choice-stone,paper,scissor   exit(for quit the game)")
print("-"*78)
print("\n")
user=0
comp=0
i=0
j=10000000000
while i<=j:
 import random
 list=['stone','paper','scissor']
 val=random.choice(list)
 a=input("User:")
 if a=="stone" or a=="paper" or a=="scissor":
  print("Computer:"+val)
 elif a=="exit":
  print("Game stopped")
 else:
  print("Enter the correct key")
 if val==a:
   print("TIE")
   print("SCORE")                                                                                                        print("user:"+str(user))
   print("computer:"+str(comp))
   print("\n")
 if val=="stone" and a=="scissor":
  print("computer won")
  comp=comp+1
  print("SCORE")
  print("user:"+str(user))
  print("computer:"+str(comp))
  print("\n")
 if val=="scissor" and a=="stone":
  print("User won")
  user=user+1
  print("SCORE")
  print("user:"+str(user))
  print("computer:"+str(comp))
  print("\n")
 if val=="scissor" and a=="paper":
  print("Computer won")
  comp+=1
  print("SCORE")
  print("user:"+str(user))
  print("computer:"+str(comp))
  print("\n")
 if val=="paper" and a=="scissor":
  print("User won")
  user+=1
  print("SCORE")
  print("user:"+str(user))
  print("computer:"+str(comp))
  print("\n")
 if val=="stone" and a=="paper":
  print("User won")
  user+=1
  print("SCORE")
  print("user:"+str(user))
  print("computer:"+str(comp))
  print("\n")
 if val=="paper" and a=="stone":
  print("Computer won")
  comp+=1
  print("SCORE")
  print("user:"+str(user))
  print("computer:"+str(comp))
  print("\n")
 if a=="exit":
  j=-1
  print("_"*78)
  print("USER                 COMPUTER")
  print(str(user)+"                    "+str(comp))
  print("\n")
i=i+1
if user>comp:
  print("USER IS THE WINNER ★★★")
else:
  print("COMPUTER IS THE WINNER ★★★")
