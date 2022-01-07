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

# 2d vector

def vector_2d(x,y):
    return math.sqrt(pow(x,2) + pow(y,2))
# 3d Vector Problem

def vector_3d(x,y,z):
    return math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))

# print(velocity_vector(-12,8,-2))

# Scalar multiplication
def scalar_multiplication(multi,x,y,z):
    return math.sqrt(pow(multi * x, 2) + pow(multi * y, 2) + pow(multi * z, 2))

# print(scalar_multiplication(3,2,-7,1))


# Dot Product 2d vector
def dot_product_2d_vector(x,y):
    return (x[0] * y[0]) + (x[1] * y[1])

# Dot Product 3d vector
def dot_product_3d_vector(x,y):
    return (x[0] * y[0]) + (x[1] * y[1]) + (x[2] + y[2])

# print(dot_product_2d_vector([-17,22],[0,32]))

# Vector angle 2d
def vector_angle_2d(x,y):
    print("First vector is %d" % (vector_2d(x[0],x[1])))
    print("Second vector is %d" % (vector_2d(y[0],y[1])))
    return dot_product_2d_vector(x,y) / (vector_2d(x[0],x[1] * vector_2d(y[0],y[1])))

# print(vector_angle_2d([-17,22],[0,32]))

# Vector angle 3d
def vector_angle_3d(x,y):
    print("First vector is %d" % (vector_3d(x[0],x[1],x[2])))
    print("Second vector is %d" % (vector_3d(y[0],y[1],y[2])))
    return dot_product_3d_vector(x,y) / (vector_3d(x[0],x[1],x[2] * vector_3d(y[0],y[1],y[2])))

# print(vector_angle_3d([3,2,-3],[0,-3,-6]))

# COMPLETE: Find count of substring occurrences in string
def count_substring(string, sub_string):
    count = 0
    sub_length = len(sub_string)
    for i in range(len(string)):
        print ('%d index' % (i))
        if string[i] == sub_string[0] and i + len(sub_string) <= len(string):
            print ('%s line 68' % (i))
            index = i
            temp_count = 0
            for sub_letter in sub_string:
                if sub_letter == string[index]:
                    temp_count += 1
                    index +=1
            if temp_count == sub_length:
                count +=1
            temp_count = 0
    return count

print(count_substring('dogloldog', 'dog'))
