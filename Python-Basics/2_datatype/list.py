tea_varities=["Black","green","masala","white"]

tea_varities[1:1]
print(tea_varities[1:1])

tea_varities[1:1]=["test","test"]
print(tea_varities)

print(tea_varities[1:2])

tea_varities[1:3]=[]

print(tea_varities)

for tea in tea_varities:
    print(tea)
    print(tea,end="-")

if "green" in tea_varities:
    print("i have it")

tea_varities.append("adrak")
print(tea_varities)
# ['Black', 'green', 'masala', 'white', 'adrak'] 

tea_varities.remove("masala")
print(tea_varities)
# ['Black', 'green', 'white', 'adrak']

tea_varities.insert(3,"chocolate")
print(tea_varities )
# ['Black', 'green', 'white', 'chocolate', 'adrak']

tea_varities_copy=tea_varities.copy()

print(tea_varities_copy)
print(id(tea_varities_copy))

# ['Black', 'green', 'white', 'chocolate', 'adrak']
# 2395715816384

print(tea_varities)
print(id(tea_varities))

# ['Black', 'green', 'white', 'chocolate', 'adrak']
# 2395713986688

squared_num=[x**2 for x in range(10)]
