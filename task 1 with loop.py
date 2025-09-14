def factorial_loop(n):
    if n < 0:
        return "factorial does not exist for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        result_ans = 1
        for i in range(2,n+1):
            result_ans = result_ans * i
        return result_ans


result=factorial_loop(int(input("Enter a number: ")))
print(result)
