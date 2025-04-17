# #counting no
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_numbers_count = 0

# for num in numbers:
#     if num>0:
#         positive_numbers_count+=1
# print("final count of postive no is", positive_numbers_count)


# # Sum of Even Numbers
# n=10
# sum_even=0

# for i in range(1,n+1):
#     if i%2==0:
#         sum_even+=1

# print(sum_even)


# #Multiplication table

# number=3

# for i in range(1,11):
#     if i==5:
#         continue
#     print(number,'x',i,'=',number*i)

# #Reverse String
# name="rohit"
# reverse_str=""

# for j in name:
#     # reverse_str= reverse_str+j
#     reverse_str=j+reverse_str
    
# print(reverse_str)

# # Non Repeated Character
# input_str="teetera"

# for char in input_str:
#     print(char)
#     if input_str.count(char)==1:
#         print("Char is:",char)
#         # break


# # Factorial
# n=5
# fact=1
# while n>0:
#     print(n)
#     fact=fact*n
#     n=n-1
# print(fact)
    
# #Valid input
# while(True):
#     number=int(input("enter a no between 1 and 10"))
#     if 1<= number <=10:
#         print("thanks")
#         break
#     else:
#         print("try again")


# #prime  no

# number=9
# is_prime= True
# if number>1:
#     for i in range(2,number):
#         if (number%i)==0:
#             is_prime=False
#             break
#         else:
#             is_prime= True
#             print("it is a prime no ", number)
#             break
#     print("not a prime no")        


# # Unique Element
# items = ["apple", "banana", "orange", "apple", "mango","mango"]

# unique_items=set()
# for item in items:
#     if item in unique_items:
#         print("dupliucate items",item)
#         # break
#     unique_items.add(item)

#Exponential backoff

import time
wait_time=1
max_tries=5
attempts=0

while attempts<max_tries:
    print("attempt", attempts+1,"- wait time", wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
