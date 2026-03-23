"""2. Write a Python program that calculates the variance and standard deviation of the dataset:
[6, 7, 8, 9, 10, 11, 12]"""

import math 

def main():
    ds = [6,7,8,9,10,11,12]
    mean = (6+7+8+9+10+11+12)/7
    print("calculate means of dataset",mean)
    
    
    for value in ds:
        sm = (value - mean)
        print("Substract mean values from ds",sm)


    sm = [-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0]
    for i in sm:

        square = i ** 2
        print("square of sm",square)


    values = [9, 4, 1, 0, 1, 4, 9]

    total = 0 
    for i in values:
        total =  total + i 
    print("sum of values",total)

    dv = total / 7 
    print("calculate dividation of all values",dv)

    sd = math.sqrt(dv)
    print("standard deviation",sd)


if __name__=="__main__":
    main()