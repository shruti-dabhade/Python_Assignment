def MarvellousLinearRegression():

    border = "-"*40

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print(border)
    print("Dataset")
    print(border)

    print("X :",X)
    print("Y :",Y)

    # Mean of X
    meanX = sum(X)/len(X)

    # Mean of Y
    meanY = sum(Y)/len(Y)

    print(border)
    print("Mean of X =",meanX)
    print("Mean of Y =",meanY)

    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i]-meanX)*(Y[i]-meanY))
        denominator = denominator + ((X[i]-meanX)**2)

    # slope
    m = numerator/denominator

    # intercept
    c = meanY - (m*meanX)

    print(border)
    print("Slope (m) =",round(m,2))
    print("Intercept (c) =",round(c,2))

    print(border)
    print("Regression Equation")
    print("Y =",round(m,2),"X +",round(c,2))

    x = 6
    predicted = (m*x) + c

    print(border)
    print("Predicted Y for X = 6 :",round(predicted,2))
    print(border)


def main():
    MarvellousLinearRegression()


if __name__=="__main__":
    main()