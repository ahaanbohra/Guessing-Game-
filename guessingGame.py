import random
chance = 0
number= random.randint(1,9)
while chance<5 :
    
    no = int(input("Guess a number between 1 and 10:"))
    if no==number:
        print("Your guess is correct, congratulations")
    elif number>no :
        print("Your guess is too low, try again")
    elif no>number :
        print("Your guess is too high, try again")    
   
    chance = chance+1   
if chance==5:
    print ("The number is" , int(number) )     
        

