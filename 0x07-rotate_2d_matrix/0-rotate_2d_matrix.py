def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise in-place."""
    n = len(matrix)  # Get the size of the matrix

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    # Print the rotated matrix
    print('[')
    for row in matrix:
        print(' ', '[', end='')
        for elem in row:
            print(str(elem) + ',', end=' ')
        print(']', end='')
        print()
    print(']')