
from datetime import datetime
now = datetime.now()

print("Current date and time:",now)
print("Formatted:",now.strftime("%Y-%M-%d %H:%M:%S"))
print("Today is:",now.strftime("%A"))

import random

secret_number = random.randint(1, 100)
attempts = 0     

print("Guess the number between 1 and 100!")

while True:  
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number: 
        print("Too low!") 
    elif guess > secret_number:
        print("Too high!") 
    else:      
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break    

from datetime import datetime
now.datetime = now()
print("Current date and time:",now)
print("Formatted:",now.strftime("%Y-%M-%d %H:%M:%S"))
print("Today is:",now.strftime("%A"))

import random
# print the random numbers
print("Enter the random numbers:",random.randint(1,100)) 

# print the random choice below the fruits
fruits=["apple","mango","litchi"]
random.choice = fruits
print("Random fruits choice:",random.choice(fruits))

# print the random shuffle numbers 
numbers = [23,234,43,35,24]
random.shuffle = numbers
print("Random the shuffle list:",random.shuffle(numbers))

import random 

secret_number = random.randint(1,100)    
attempts = 0

print("Enter the guessing number 1 and 100:")
while  True: 
    guess = (int(input("Your guess:" )))

if guess < secret_number: 
    print("Too Low")

elif guess > secret_number:
    print("Too High!")

else:
    print(f"Congratulations, you guessed it in {attempts} attempts")

import random       
# Random integer between 1 and 100
print("Random numbers:",random.randint(1, 100))

# Random Fruits choice
fruits= ["apple","banana","litchi","mango"] 
print("Random fruit name : ", random.choice(fruits))

# Random shuffle the numbers
numbers = [23, 56, 23, 65, 37] 
random.shuffle(numbers)
print("Random shuffle list: ",numbers)
