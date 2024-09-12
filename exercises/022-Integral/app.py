# Your code here
def squares_dictionary(n):
    dicc={}
    for x in range(1,n+1):
        dicc[x] =x*x
    return dicc

print (squares_dictionary(9))