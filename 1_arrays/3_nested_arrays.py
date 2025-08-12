## Working with 2D and nested lists: access, modify, flatten, transpose, row/col extraction

def create_2d_array():
    return [[1, 2], [3, 4], [5, 6]]

def access_element(matrix, row, col):
    return matrix[row][col]

def update_element(matrix, row, col, value):
    matrix[row][col] = value
    return matrix

def flatten_matrix(matrix):
    return [elem for row in matrix for elem in row]

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def get_row(matrix, row_index):
    return matrix[row_index]

def get_column(matrix, col_index):
    return [row[col_index] for row in matrix]

def add_row(matrix, new_row):
    matrix.append(new_row)
    return matrix

def remove_row(matrix, index):
    if 0 <= index < len(matrix):
        matrix.pop(index)
    return matrix

def matrix_dimensions(matrix):
    return len(matrix), len(matrix[0]) if matrix else 0

if __name__ == "__main__":
    m = create_2d_array()
    print("Original:", m)
    print("Access (1,1):", access_element(m, 1, 1))
    print("Updated (0,0):", update_element(m, 0, 0, 9))
    print("Flattened:", flatten_matrix(m))
    print("Transposed:", transpose_matrix(m))
    print("Row 0:", get_row(m, 0))
    print("Column 1:", get_column(m, 1))
    print("Add row:", add_row(m, [7, 8]))
    print("Remove row 1:", remove_row(m, 1))
    print("Dimensions:", matrix_dimensions(m))