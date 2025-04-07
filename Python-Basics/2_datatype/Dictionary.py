# declaring dictionary
chai_types= {"Masala":"Spicy", "Ginger":"Zesty", "Green":"Mild"}

print(chai_types["Masala"])

print(chai_types.get("Ginger"))
print(chai_types.get("Gingery")) #return None

# get returns

for chai in chai_types:
    print(chai)  #gives only key
    print(chai,chai_types[chai])


#for key,value in chai_types.items() = when ititating over dictionary

for key, value in chai_types.items():
    print(key,value)


if "Masala" in chai_types:
    print("i have masala chai ")


print(len(chai_types))


chai_types["mojito"]= "citrus"
print(chai_types)

chai_types.pop("Ginger")
print(chai_types) 

print(chai_types.popitem())

del chai_types["Green"]
print(chai_types) 

chai_types_copy= chai_types.copy()

squar_num={x:x**2 for x in range(6) }
print(squar_num)

squar_num.clear() #to clear squar_num

keys = ["Masala","Ginger","lemon"]
default_value= "Delicious"

new_dict=dict.fromkeys(keys, default_value)
print(new_dict)