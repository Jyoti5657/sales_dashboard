import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)   # 100 points from 0 to 10
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue', linewidth=2, label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.legend() 
plt.show ()  

import random
# Random number within 1 to 100
print("Random numbers:",random.randint(1 , 100))

# Random choice 
fruits=["apple","litchi","orange"]
print("Random fruits name",random.choice(fruits))

# Random shuffle numbers
numbers=[64,78,23,44,22]
random.shuffle(numbers)
print("Random shuffle list:",numbers)

import pandas as pd 
 
# Create a simple DataFrame  
data = { 
    'Name': ['Alice', 'Bob','Charlie'],      
    'Age': [25, 30, 35],                           
    'City': ['New York', 'London', 'Paris']               
}                                                                                                                   
df = pd.DataFrame(data=StopAsyncIteration)  
print("Data Table:\n", df) 
# Basic operations 
print("\nAverage age:", df['Age'].mean()) 
print("People older than 28:\n", df[df['Age'] > 28]) 

from datetime import datetime 
now = datetime.now()  

print("Current date and time:",now)
print("Formatted:",now.strftime("%Y-%M-%d %H:%M:%S"))  
print("Today is:",now.strftime("%A"))  

import random
secret_number = random.randint(1,100)
attempts = 0

print(" ")

from datetime import datetime
now = datetime.now() 

print("Current date and time",now)
print("Formatted:",now.strftime("%Y-%M-%d %H:%M:%S"))
print("Today is:",("%A"))   

if __name__ == "__main__":
  array=[56,23,45,76,67]

  print("Sorted array:")            
  

