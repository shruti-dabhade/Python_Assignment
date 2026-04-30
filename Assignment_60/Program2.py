"""2: Write a Python program to demonstrate ReLU and Max Pooling."""

# ---------------------------------------------------------
# Q2 : ReLU and Max Pooling
# ---------------------------------------------------------

def print_matrix(mat):
    for row in mat:
        print(row)

def relu(x):
    return max(0, x)

def relu_and_pooling():

    print("\n========= ReLU AND MAX POOLING =========\n")

    feature_map = [
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ]

    print("Original Feature Map:")
    print_matrix(feature_map)

    # ReLU
    relu_output = []
    for row in feature_map:
        relu_output.append([relu(x) for x in row])

    print("\nAfter ReLU:")
    print_matrix(relu_output)

    # Max Pooling (2x2)
    pooled = []
    for i in range(0, len(relu_output)-1, 2):
        row = []
        for j in range(0, len(relu_output[0])-1, 2):

            block = [
                relu_output[i][j],
                relu_output[i][j+1],
                relu_output[i+1][j],
                relu_output[i+1][j+1]
            ]

            max_val = max(block)
            row.append(max_val)

        pooled.append(row)

    print("\nAfter 2x2 Max Pooling:")
    print_matrix(pooled)

    print("\nExplanation:")
    print("Pooling reduces size by taking only important (max) values.")


if __name__ == "__main__":
    relu_and_pooling()