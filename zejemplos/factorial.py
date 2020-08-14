# def factorial(numero):
#   fact=1
#   for i in range(2,numero+1):
#     fact*=i
#   return fact

def factorial(numero):
    if numero == 1:
        return 1
    return factorial(numero-1)*numero

print(factorial(5))
