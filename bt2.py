def read_number_from_file(filename):
    try: 
        with open(filename, 'r') as file:
            numbers = list(map(int, file.read().split()))
            return numbers
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
def write_number_to_file(numbers, filename):
    try:
        with open(filename, 'w') as file:
            for number in numbers:
                file.write(str(number) + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")
def find_same_number(file1, file2, file3):
    numbers1 = read_number_from_file(file1)
    numbers2 = read_number_from_file(file2)
    numbers3 = read_number_from_file(file3)
    # same_numbers = []
    # for number1 in numbers1:
    #     for number2 in numbers2:
    #         for number3 in numbers3:
    #             if number1 == number2 and number2 == number3:
    #                 same_numbers.append(number1)
    set1 = set(numbers1)
    set2 = set(numbers2)
    samenumbers = set1.intersection(set2)
    write_number_to_file(sorted(samenumbers), file3)
    #return same_numbers
def __main__():
    file1 = 'Num1.txt'
    file2 = 'Num2.txt'
    file3 = 'Result.txt'
    find_same_number(file1, file2, file3)

__main__()