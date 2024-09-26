def process_file(file_path, output_path, output_format):
    with open(file_path, 'r') as file, open(output_path, 'w') as output_file, open(output_format, 'w') as format_file:
        for line_number, line in enumerate(file, start=0):
            if line_number == 0:
                continue
            numbers = list(map(float, line.split()))
            row_sum = sum(numbers)
            num_elements = len(numbers)
            output_file.write(f"Customer_id {line_number}: Count of elements = {num_elements}, Sum = {row_sum}\n")
            print(f"Customer_id {line_number}: Count of elements = {num_elements}, Sum = {row_sum}")
            if num_elements > 5 or row_sum > 20:
                format_file.write(f"Customer_id {line_number}: Count of elements = {num_elements}, Sum = {row_sum}\n")
                print(f"CUstomer_id {line_number}: Count of elements = {num_elements}, Sum = {row_sum}")
def __main__():
    file_path = 'KHACHBAY.VAO'
    output_path = 'TRONGLUONG.RA'
    output_format = 'HUYBAY.RA'
    process_file(file_path, output_path, output_format)

__main__()