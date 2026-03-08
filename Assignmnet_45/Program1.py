
import csv
import math
import random


def EucDistance(p1,p2):
    Ans = math.sqrt((p1['X'] - p2['X'])**2 + (p1['Y'] - p2['Y'])**2)
    return Ans


def GetData(FileName):

    data = []

    file = open(FileName,'r')
    reader = csv.reader(file)

    next(reader)

    for row in reader:

        temp = {}

        temp['X'] = float(row[1])      # Alcohol
        temp['Y'] = float(row[2])      # Malic acid
        temp['label'] = row[0]         # Class

        data.append(temp)

    return data


def PrepareData(data):

    random.shuffle(data)

    size = int(len(data) * 0.7)

    TrainData = data[:size]
    TestData = data[size:]

    return TrainData,TestData


def MarvellousKneighboursClassifier(TrainData,new_point,k):

    border = "-"*40

    # calculate distance
    for d in TrainData:
        d['distance'] = EucDistance(d,new_point)

    print(border)
    print("Calculated distances are :")
    print(border)

    for d in TrainData:
        print(d)

    sorted_data = sorted(TrainData,key=lambda item:item['distance'])

    print(border)
    print("Sorted data is :")
    print(border)

    for d in sorted_data:
        print(d)

    nearest = sorted_data[:k]

    print(border)
    print("Nearest elements are :")
    print(border)

    for d in nearest:
        print(d)

    # Voting
    votes = {}

    for neighbour in nearest:

        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1

    print(border)
    print("Voting result is :")
    print(border)

    for v in votes:
        print("Name :",v,"Number of votes :",votes[v])

    result = max(votes,key=votes.get)

    return result


def CalculateAccuracy(TrainData,TestData):

    correct = 0
    k = 3

    for t in TestData:

        new_point = {'X':t['X'],'Y':t['Y']}

