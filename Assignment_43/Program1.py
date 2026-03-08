import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def CheckAccuracy(data, target):

    border = "-"*40

    X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size=0.5)

    for k in [1,3,5]:

        model = KNeighborsClassifier(n_neighbors = k)

        model.fit(X_train, Y_train)

        prediction = model.predict(X_test)

        acc = accuracy_score(Y_test, prediction)

        print(border)
        print("Accuracy for K =",k,"is :",acc)


def MarvellousPlayPredictor():

    border = "-"*40

    print(border)
    print("Loading dataset")
    print(border)

    df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    print(df)

    print(border)
    print("Preparing data")
    print(border)

    le = LabelEncoder()

    df['Wether'] = le.fit_transform(df['Wether'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])

    print(df)

    X = df[['Wether','Temperature']]
    Y = df['Play']

    print(border)
    print("Training KNN Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(X,Y)

    print(border)
    print("Testing Model")
    print(border)

    wether = int(input("Enter Wether (0-Sunny 1-Overcast 2-Rainy): "))
    temp = int(input("Enter Temperature (0-Hot 1-Mild 2-Cold): "))

    result = model.predict([[wether,temp]])

    if result == 1:
        print("Play : Yes")
    else:
        print("Play : No")

    print(border)
    print("Calculating Accuracy")
    print(border)

    CheckAccuracy(X,Y)


def main():
    MarvellousPlayPredictor()


if __name__ == "__main__":
    main()