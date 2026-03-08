def MarvellousModelPerformance():

    border = "-"*40

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    meanX = sum(X)/len(X)
    meanY = sum(Y)/len(Y)

    num = 0
    den = 0

    for i in range(len(X)):
        num = num + ((X[i]-meanX)*(Y[i]-meanY))
        den = den + ((X[i]-meanX)**2)

    m = num/den
    c = meanY - (m*meanX)

    print(border)
    print("Predicted Y values")
    print(border)

    predicted = []

    for i in range(len(X)):
        y = m*X[i] + c
        predicted.append(y)
        print("Actual :",Y[i]," Predicted :",round(y,2))

    # MSE
    error = 0

    for i in range(len(Y)):
        error = error + (Y[i]-predicted[i])**2

    mse = error/len(Y)

    print(border)
    print("Mean Squared Error :",round(mse,2))

    # R2
    ss_total = 0
    ss_res = 0

    for i in range(len(Y)):
        ss_total = ss_total + (Y[i]-meanY)**2
        ss_res = ss_res + (Y[i]-predicted[i])**2

    r2 = 1 - (ss_res/ss_total)

    print("R2 Score :",round(r2,2))
    print(border)


def main():
    MarvellousModelPerformance()


if __name__=="__main__":
    main()