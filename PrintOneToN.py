"""
print 1 to n using recursion
"""
def printNatural(n):
    if(n > 0):
        printNatural(n-1)
        print(n, end = " ")

n = int(input("enter the N value :"))
printNatural(n)
