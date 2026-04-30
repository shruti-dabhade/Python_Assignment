"""1: Write a Python program to manually perform convolution."""

# ---------------------------------------------------------
# Q1 : Manual Convolution
# ---------------------------------------------------------

def print_matrix(mat):
    for row in mat:
        print(row)

def convolution():

    print("\n========= MANUAL CONVOLUTION =========\n")

    # Input Image (5x5)
    image = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # Kernel (3x3)
    kernel = [
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ]

    print("Input Image:")
    print_matrix(image)

    print("\nKernel:")
    print_matrix(kernel)

    feature_map = []

    # Convolution
    for i in range(3):  # 5-3+1 = 3
        row = []
        for j in range(3):

            print(f"\nRegion at position ({i},{j}):")

            total = 0

            for ki in range(3):
                for kj in range(3):

                    val = image[i+ki][j+kj]
                    k = kernel[ki][kj]
                    mul = val * k

                    print(f"{val}*{k} =", mul)

                    total += mul

            print("Output =", total)
            row.append(total)

        feature_map.append(row)

    print("\nFeature Map:")
    print_matrix(feature_map)


if __name__ == "__main__":
    convolution()