
var = 1461501637330902918203684832716283019655932542975
def isPower (x, y):
     
    # The only power of 1
    # is 1 itself
    if (x == 1):
        return (y == 1)
         
    # Repeatedly compute
    # power of x
    pow = 1
    while (pow < y):
        pow = pow * x
 
    # Check if power of x
    # becomes y
    return (pow == y)
# print(len(str(var)))
for i in range(2,1000000):
    result = var%i
    if result == 0:

        # print(True,i)
        res = var//i
        for j in range(2,1000000):
            newResult = res % j
            if newResult == 0:
                print(newResult)
                print(hex(newResult),len((hex(newResult))))
                print("--------------")
                newVar = newResult * i
                print(newVar)
            # if int(newVar * i) == var:
            #     print(True)
            # print(len((str((var/i).hex()))))
            break
        # pass
# print(6%2)


