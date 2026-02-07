"""
Script that converts decimal numbers into it's binary and hexadecimal value
"""
import time
import sys

def convert2bin(number: int) -> str:
    """
    Converts given decimal number into it's binary expression
    
    :param number: Input Number
    :type number: int
    :return: Binary conversion
    :rtype: str
    """
    if number < 0:
        is_negative = True
        number = -number
    else:
        is_negative = False

    if number == 0:
        binary = "0"
    else:
        binary = ""
        while number > 0:
            rem = number % 2
            binary = str(rem) + binary
            number = number // 2

    if is_negative:
        # Add padding to 10 bits
        while len(binary) < 10:
            binary = "0" + binary

        # Invert bits
        inverted = ""
        for bit in binary:
            if bit == "0":
                inverted += "1"
            else:
                inverted += "0"

        # Add 1 to the complement
        carry = 1
        result = ""

        for i in range(9, -1, -1):
            bit_sum = int(inverted[i]) + carry

            if bit_sum == 2:
                result = "0" + result
                carry = 1
            else:
                result = str(bit_sum) + result
                carry = 0
        binary = result

    return binary

def convert2hex(number: int) -> str:
    """
    Converts given decimal input number into it's hexadecimal expression
    
    :param number: Input Number
    :type number: int
    :return: Hexadecimal conversion
    :rtype: str
    """
    hex_digits = "0123456789ABCDEF"
    bin_n = convert2bin(number)
    hexadecimal = ""

    if number == 0:
        hexadecimal = "0"
    elif number > 0:
        while number > 0:
            rem = number % 16
            hexadecimal = hex_digits[rem] + hexadecimal
            number = number // 16
    else:
        # Convert into 12 bits
        bin_n = "11" + bin_n
        for i in range(0, 9, 4):
            group = bin_n[i:i+4]
            value = 0

            # Convert 4-bit binary to decimal
            power = 3
            for bit in group:
                value += int(bit) * (2 ** power)
                power -= 1

            hexadecimal += hex_digits[value]

        # Pad into 10 bits
        while len(hexadecimal) < 10:
            hexadecimal = "F" + hexadecimal

    return hexadecimal

def read_file(filename: str) -> list:
    '''
    Reads file from a specified path and returns content 
    
    :param filename: File path
    :type filename: str
    :return: List of lines inside the file
    :rtype: list
    '''
    content_list = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            try:
                content_list.append(int(line.strip()))
            except ValueError:
                print(f"Your file contains invalid character/s ({line}) skipping...")

    return content_list

def save_data(input_dict: dict, timestamp: float):
    """
    Docstring for save_data
    
    :param input_dict: Description
    :type input_dict: dict
    :param timestamp: Description
    :type timestamp: float
    """
    with open('ConvertionResults.txt', 'w', encoding="utf-8") as new_file:
        new_file.write("Decimal      Binary      Hexadecimal\n")
        for key in input_dict.keys():
            new_file.write(f"{key}      {input_dict[key][0]}      {input_dict[key][1]}\n")

        new_file.write(f"\n**** Program took {timestamp} seconds to run ****")


if __name__ == "__main__":
    init_time = time.time()

    args = sys.argv
    INPUT_FILE = str(args[1])
    num_list = read_file(INPUT_FILE)
    results_dict = {}
    print("Decimal    Binary    Hexadecimal")

    for num in num_list:
        bin_num = convert2bin(num)
        hex_num = convert2hex(num)
        results_dict[num] = (bin_num, hex_num)
        print(f"{num}      {bin_num}      {hex_num}")

    end_time = time.time()
    duration = end_time - init_time
    save_data(results_dict, duration)
    print(f"**** Program took {duration} seconds to run ****")
