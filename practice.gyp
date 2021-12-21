import math
number1 = 20
number2 = 30

# def product_or_sum(n1,n2):

#     if n1 * n2 > 1000:
#         return n1 * n2
#     else:
#         return n1 + n2

# print(product_or_sum(number1,number2))

# Velocity Vector Problem

def velocity_vector(x,y,z):
    return math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))

# print(velocity_vector(-12,8,-2))

# Scalar multiplication
def scalar_multiplication(multi,x,y,z):
    return math.sqrt(pow(multi * x, 2) + pow(multi * y, 2) + pow(multi * z, 2))

print(scalar_multiplication(3,2,-7,1))