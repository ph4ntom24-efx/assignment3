def factorial_recursion(n):

    if n < 0:
        return "factorial does not exist for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial_recursion(n-1)

result = factorial_recursion(int(input("Enter a number: ")))
print(result)
