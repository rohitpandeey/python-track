# Revision

def even(n):
    for i in range(2,n+1,2):
        yield i

for num in even(10):
    print(num)