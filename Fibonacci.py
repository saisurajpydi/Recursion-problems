"""
fibonacci - 0,1,1,2,3,5,8,13,21.....
"""
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = int(input("enter the N value to print N fibonacci :" ))
for i in range(n):
    print(fibonacci(i), end = " ")