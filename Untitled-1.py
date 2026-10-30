# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum_result}")

# from datetime import datetime 
# now = datetime.now()

# print("Current date and time:",now)
# print("Formatted:",now.strftime("%y-%M-%d %H:%M:%S"))
# print("Today is:",now.strftime("%A"))

# import random
# secret_number = random.randint(1,100)
# attempts = 0 

# print("Enter the guessed number within 1 and 100:")

# while True:
#      guess = (int(input("Your guess:")))
#      attempts += 1  

#      if guess < secret_number:
#           print(" Too Low!!")

#      elif guess > secret_number:
#           print(" Too High!!")
#      else:
#           print(f"Congratulations, you guessed it in {attempts} attempts")                  


import random        
    # Random integer between 1 and 100
print("Random number:", random.randint(1, 100))

    # Random choice from a list
fruits=["apple","litchi","pear"]
random.choice = fruits
print("Enter the random choice from the fruits",(fruits))

     # Random shuffle number 
numbers=[89,32,33,45,56]
random.shuffle = numbers
print("Random shuffle list", numbers)

import random
secret_number = random.randint(1,100)
attempts = 0

print("Enter the guessed number within 1 and 100:")
while True:
          guess = (int(input("Your guess:")))
          attempts += 1

          if guess < secret_number:
               print("Too Low!")

          elif guess > secret_number:
                print("Too High!")

          else:
               print(f"Congrats!, you guessed it in {attempts} attempts")
               break

 
          # from datetime import datetime
          # now = datetime.now()

          # print("Current date and time:",now)
          # print("Formatted:",now.strftime("%Y-%M-%d %H:%M:%S"))
          # print("Today is:",now.strftime("%A"))

          



           
         



    
