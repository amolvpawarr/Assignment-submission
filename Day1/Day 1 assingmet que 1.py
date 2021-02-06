#  using if condition
num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
operation = input()           ## choose operation 
if operation == 'add':
    sum = num1 + num2
    print(sum)
elif operation == 'sub':
    differnce = num1 - num2
    print(differnce)
elif operation == 'mul':
    product = num1 * num2
    print(product)
elif operation == 'div':
    result = num1 / num2
    print(result)
else:
    print('-1')
    

