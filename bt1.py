def create_matrix(n):
    matrix = []
    print(f"Enter the elements of {n}x{n} matrix row wise:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Element of [{i}][{j}]: ")))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))  # Print each row nicely

def write_matrix_rowfirst_rowthrid(matrix, filename):
    with open(filename, "w") as file:  # Open the file in write mode
        for i in range(len(matrix)):
            if i == 0 or i == 3:  # Check if the row is the first or fourth
                file.write(" ".join(map(str, matrix[i])) + "\n")  # Write the row

def write_matrix(matrix, filename):
    with open(filename, "w") as file:  # Open the file in write mode
        for row in matrix:
            file.write(" ".join(map(str, row)) + "\n")  # Write each row

def find_odd_number(matrix, filename):
    with open(filename, "w") as file:  # Open the file in write mode
        for row in matrix:
            for num in row:
                if num % 2 != 0:
                    file.write(str(num) + " ")
                else:
                    file.write("0 ")
            file.write("\n")

def read_number_from_file(filename):
    try:
        with open(filename, 'r') as file:
            matrix = []
            for line in file:
                row = list(map(int, line.split()))
                matrix.append(row)
            print("Matrix from file:")
            for row in matrix:
                print(" ".join(map(str, row)))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def __main__():
    n = int(input("Enter n = "))
    matrix = create_matrix(n)
    print("Original Matrix:")
    print_matrix(matrix)

    # Write the entire matrix to a file
    write_matrix(matrix, "input.txt")
    
    # Write specific rows to another file
    write_matrix_rowfirst_rowthrid(matrix, "Sole.txt")
    
    # Find odd numbers and write to file
    find_odd_number(matrix, "Sole.txt")

    # Read the matrix back from the file and print it
    read_number_from_file("Sole.txt")

__main__()
