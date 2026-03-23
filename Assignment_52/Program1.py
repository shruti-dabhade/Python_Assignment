"""Cluster students into different academic performance groups based on features like:"""

import pandas as pd
from sklearn.cluster import KMeans

def main():
    # Load dataset
    df = pd.read_csv("student-mat.csv")

    print("Dataset Loaded Successfully")
    print(df.head())

    # Select required features
    X = df[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

    print("\nSelected Features:")
    print(X.head())

    # Apply KMeans (3 clusters)
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    print("\nCluster Assigned Data:")
    print(df[['G1','G2','G3','studytime','failures','absences','Cluster']].head())

    # Group analysis
    print("\nCluster Summary:")
    print(df.groupby('Cluster').mean())

    # Label clusters manually
    for i in range(3):
        print("\nCluster", i, "Details:")
        print(df[df['Cluster'] == i].head())

if __name__ == "__main__":
    main()