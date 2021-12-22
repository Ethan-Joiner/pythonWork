import math
number1 = 20
number2 = 30
# The fundamental building blocks of linear algebra are vectors. Vectors are defined as quantities having both direction and magnitude, compared to scalar quantities that only have magnitude. In order to have direction and magnitude, vector quantities consist of two or more elements of data. The dimensionality of a vector is determined by the number of numerical elements in that vector. For example, a vector with four elements would have a dimensionality of four.

# Let’s take a look at examples of a scalar versus a vector. A car driving at a speed of 40mph is a scalar quantity. Describing the car driving 40mph to the east would represent a two-dimensional vector quantity since it has a magnitude in both the x and y directions.
# An important vector operation in linear algebra is the dot product. A dot product takes two equal dimension vectors and returns a single scalar value by summing the products of the vectors’ corresponding components.

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


# Dot Product
def dot_product_2d_vector(x,y):
    return (x[0] * y[0]) + (x[1] + y[1])

print(dot_product_2d_vector([-17,22],[0,32]))