"""3: Write a Python program to show flattening."""

# ---------------------------------------------------------
# Q3 : Flattening in CNN
# ---------------------------------------------------------

def flattening():

    print("\n========= FLATTENING =========\n")

    matrix = [
        [6, 4],
        [8, 6]
    ]

    print("Input Matrix:")
    for row in matrix:
        print(row)

    # Flatten
    flatten_output = []
    for row in matrix:
        flatten_output.extend(row)

    print("\nFlatten Output:", flatten_output)

    # Fully connected layer (manual)
    weights = [0.2, 0.3, 0.4, 0.1]
    bias = 0.5

    print("\nWeights:", weights)
    print("Bias:", bias)

    # Dot product
    z = sum(x*w for x, w in zip(flatten_output, weights)) + bias

    print("\nFinal Output (after FC layer):", z)

    print("\nExplanation:")
    print("Flatten converts 2D data into 1D vector to feed into dense layer.")


if __name__ == "__main__":
    flattening()