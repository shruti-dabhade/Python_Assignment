import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def MarvellousAdvertisingPredictor():

    border = "-" * 40

    print(border)
    print("Loading Dataset")
    print(border)

    df = pd.read_csv("Advertising.csv")

    print(df.head())

    print(border)
    print("Preparing Data")
    print(border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print(border)
    print("Training Linear Regression Model")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    print(border)
    print("Testing Data")
    print(border)

    prediction = model.predict(X_test)

    print(border)
    print("Actual Values   Predicted Values")
    print(border)

    for i in range(len(prediction)):
        print("Actual :",Y_test.iloc[i]," Predicted :",prediction[i])


def main():
    MarvellousAdvertisingPredictor()


if __name__ == "__main__":
    main()