"""
print the n to 1 for a given n
"""
def printval(n):
    if(n > 0):
        print(n , end = " ")
        printval(n-1)

n = int(input("enter the N value :"))
printval(n)