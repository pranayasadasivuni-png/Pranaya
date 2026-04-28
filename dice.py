#Roll the dice?(y/n)
import random
while True:
    a = input("Roll the dice (y/n):").lower()

    if a =='y':
      dice1=random.randint (1, 6)
      dice2=random.randint (1, 6)
      print(f'({dice1}), ({dice2})')
    elif a=='n':
     print("Thanks for playing!")
     break
    else:
        print("Invalid input")   
