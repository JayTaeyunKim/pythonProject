def factorial(num):
    if num==0:
        return 0
    if num==1:
        return 1
    return factorial(num-1)*num

def combination(a, b):
    return factorial(a)/(factorial(a-b)*factorial(b))

print(combination(52, 7))