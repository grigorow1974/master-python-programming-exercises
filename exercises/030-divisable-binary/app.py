# Your code here
def divisible_binary(binary):
    binary = list(binary.split(","))
    for x in binary:
        decimal = int(x)
        if decimal % 5 ==0:
            print (decimal)

divisible_binary("1000,1100,1010,1111")
            