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


#Multiplication table

number=3

for i in range(1,11):
    if i==5:
        continue
    print(number,'x',i,'=',number*i)

#Reverse String
name="rohit"
reverse_str=""

for j in name:
    # reverse_str= reverse_str+j
    reverse_str=j+reverse_str
    
print(reverse_str)

