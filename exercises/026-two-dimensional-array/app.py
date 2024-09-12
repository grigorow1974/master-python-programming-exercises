# Your code here
def two_dimensional_list(x,y):
    arr = [[i*j for i in range(y)] for j in range(x)]
    return arr


print(two_dimensional_list(3,5))
