
import math
var = 1461501637330902918203684832716283019655932542975

# x = 1461501637330902918203684832716283019655932542975/

for i in range(100000000):
    y = math.sqrt(var)
    result = y * y
    if var == result:
        print(True,y)
        break
    var = var - i

    # if type(y) == int:
    #         print("int")
    #         print(i)
    #         print(y)
    # x = x - i

    # print(int(y))

    # if y * y == x:
    


