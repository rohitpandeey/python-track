# #1 Age group

# age=int(input("enter a age"))
# if age<13:
#     print("child")
# elif age<20:
#     print("Teenager")
# elif age <60:
#     print("Adult")
# else:
#     print("senior")

# # Movie Ticket 

# age_movie= int(input("enter your age"))
# day= input("Enter day")

# price= 12 if age >= 18 else 8

# if day=="Wednesday":
#     price=price-2

# print("ticket price for you is $",price)

# #Grade caalculator
# score=300
# if score>=101:
#     print("enter valid no")
#     exit()

# if score>=90:
#     grade="A"
# elif score>=80:
#     grade="B"
# elif score>=70:
#     grade="C"
# elif score>=60:
#     grade="D"
# else:
#     grade="F"


# print(grade)

# #Fruit RIpe 
# color="green"
# fruit="banana"

# if color not in ["green","yellow","brown"]:
#     print("exit")
#     exit()
# if fruit=="banana":
#     if color=="green":
#         print("Unripe")
#     elif color=="yellow":
#         print("ripped")
#     else:
#         print("overriped")


# # Weather activity

# weather="sunny"

# if weather=="sunny":
#     activity="Go for a walk"
# elif weather=="rainy":
#     activity="read a book"
# else:
#     activity="build a snowman"

# print(activity)


# # Transport
# distance=5
# if distance<3:
#     transport="walk"
# elif distance<15:
#     transport="bike"
# else:
#     transport="car"

# print(transport)


#coffee
# order_size="small"
# extra_shot=True


# if extra_shot:
#     coffee= order_size + "coffee with an extra shot"
# else:
#     coffee=order_size+"coffee"

# print(coffee)


#password check

password="Secure2p@ss"
if len(password)<6:
    strength="weak"
elif len(password)<10:
    strength="medium"
else:
    strength="strong"

print("password strength is:",strength)


#leap year checker 
year= 2024

if (year%400==0) or (year %4 ==0 and year%100 != 0):
    print("it is leap year")
else:
    print("not a leap year")




