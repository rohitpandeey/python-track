x = 12  # Create an integer object with value 12
print(id(x))  # Print the memory address of x 11758344
y = x  # This gives memory reference to same integer object 
print(id(y))  # This will show same memory address as x 11758344
x=5
print(id(x)) # This will show a different memory address 11758120


myD= {'one':'lemon','two':'banana','three':'apple'}
print(myD['one'])


import math
math.pi

import random
random.choice([1,2,3,4,5,6]) #gives random no among these five no's


parts = []
for i in range(10000):
    parts.append(str(i))  # Modifies the existing list
result = "".join(parts)
print(parts) 

# String
chai="Masala Chai"
slice_chai= chai[0:6]
print(slice_chai)


num_list="0123456789"
num_list[0:7:2] 
# '0246' hoping of 1
num_list[0:7:3]
# hoping of 2 digit


print(chai.lower())

print(chai.strip)  # same like trim method in js
print(chai.replace("Masala","Ginger")) #replaces masala with ginger but don't change anything in main as it is immutable

chai_love= "lemon, Ginger, Masala, Mint"
print(chai_love.split(", ")) # List meh convert krne k liye, jaha pe coma nad space hoga vha  operation hoga

print(chai.find("Chai"))

print(chai.count("Chai")) #kitne bar chai aya btayega

chai_type="Masala"
quantity=2
order=" I ordered {} cups of {} chai"

print(order.format(quantity, chai_type)) # similar function as ${} in JS

chai_variety= ["Lemon", "Masala", "Ginger"]
chai_variety

print("".join(chai_variety)) #LemonMasalaGinger
print(" ".join(chai_variety)) #Lemon Masala Ginger
print(", ".join(chai_variety)) #Lemon, Masala, Ginger


print(len(chai))


chai = "he said, \" Masala Chai is Awesome\" "