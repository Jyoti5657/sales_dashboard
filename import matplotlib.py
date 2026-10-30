# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

import random
print("Random the numbers:",random.randint(1,100))

import random
secret_number = random.randint( 1, 100)  
attempts = 0  

print("Enter the guessed number within 1 and 100") 
 
while True: 
    guess = (int(input("your guess:"))) 
    attempts += 1 

    if guess < secret_number:  
     print("Too Low !")  
 
    elif  guess > secret_number:   
       print("Too High!")                                                       

    else: 
     print(f"Congratulations, you guessed it in {attempts} attempts.")   
    break                                                                

import matplotlib.pyplot as plt 
import numpy as np  
 
plt.style.use('_mpl-gallery') 

# make the data 
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
# size and color: 
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot  
fig, ax = plt.subplots() 

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100) 
 
ax.set(xlim=(0,8), xticks=np.arange(0,8), 
       ylim=(15,80),yticks=np.arange(0,8))        
plt.show()    

# from datetime import datetime
# now = datetime.now() 

# print("Current date and time:",now) 
# print("Formatted:",now.strftime("%Y-%M-%d %H:%M:%S"))
# print("Today is:",now.strftime("%A"))

# import numpy as np 

# # Create arrays                
# arr1 = np.array([1, 2, 3, 4, 5]) 
# arr2 = np.array([10, 20, 30, 40, 50]) 

# print("Array 1:", arr1)      
# print("Array 2:", arr2)    

# print("Sum of arrays:", arr1 + arr2 ) 
# print("Mean:", np.mean(arr1))
# print("Maximum value:", np.max(arr1)) 
# print("2D array:\n", np.array([[1, 2], [3, 4]])) 
 
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 10, 100)   # 100 points from 0 to 10
# y = np.sin(x) 

# plt.figure(figsize=(8, 5))
# plt.plot(x, y, color='blue', linewidth=2, label='sin(x)') 
# plt.title('Sine Wave') 
# plt.xlabel('X axis') 
# plt.ylabel('Y axis')   
# plt.grid(True) 
# plt.legend() 
# plt.show() 



