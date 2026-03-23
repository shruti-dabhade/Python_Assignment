"""1. Write a Python program that calculates the mean of a dataset using NumPy for the following values:
[6, 7, 8, 9, 10, 11, 12]"""

import numpy as np 

def main():
    ds = [6,7,8,9,10,12]
    mean_value = np.mean(ds)

    print("mean :", mean_value)



if __name__=="__main__":
    main()