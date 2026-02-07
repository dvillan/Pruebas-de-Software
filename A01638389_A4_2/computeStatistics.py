"""
Script dedicated to compute basic statistics
"""
import time
import sys
import math

def compute_median(number_list: list) -> float:
    """
    Returns the median of a given list of numbers
    
    :param number_list: List of numbers 
    :type number_list: list
    :return: Median of all numbers 
    :rtype: float
    """
    number_list.sort()
    n = len(number_list)
    mid = n // 2

    if n % 2 == 0:
        median = number_list[mid]
    else:
        median = (number_list[mid-1] + number_list[mid]) / 2

    return median

def compute_mean(number_list: list) -> float:
    """
    Returns the mean of a given list of numbers
    
    :param number_list: List of numbers
    :type number_list: list
    :return: Mean of all numbers
    :rtype: float
    """
    total = 0
    count = 0

    for number in number_list:
        total += number
        count += 1

    mean = total / count

    return mean

def compute_mode(number_list: list) -> int:
    """
    Returns the mode of a given list of numbers
    
    :param number_list: List of numbers
    :type number_list: list
    :return: Mode of all numbers
    :rtype: int
    """
    mode = int(max(set(number_list), key=number_list.count))

    return mode

def compute_std(number_list: list) -> float:
    """
    Returns the standard deviation of a given list of numbers
    
    :param number_list: List of numbers
    :type number_list: list
    :return: Standard Deviation of all numbers
    :rtype: float
    """
    n = len(number_list)
    mean = compute_mean(number_list)
    upper = 0
    for num in number_list:
        upper += (num - mean)**2

    std = math.sqrt(upper/(n-1))

    return std

def compute_variance(number_list: list) -> float:
    """
    Returns the standard deviation of a given list of numbers
    
    :param number_list: List of numbers
    :type number_list: list
    :return: Variance of all numbers
    :rtype: float
    """
    std = compute_std(number_list)
    variance = std ** 2

    return variance

def save_data(input_dict: dict, timestamp: float):
    """
    Saves data from a given dictionary into a file 

    :param input_map: Description
    :type input_map: dict
    """
    with open("StatisticsResults.txt", "w", encoding="utf-8") as new_file:
        for key in input_dict.keys():
            print(f"{key}    {input_dict[key]}")
            new_file.write(f"{key}    {input_dict[key]}\n")

        new_file.write(f"\n**** Program took {timestamp} seconds to run ****")

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
                content_list.append(float(line.strip()))
            except ValueError:
                print(f"Your file contains invalid character/s ({line}) skipping...")

    return content_list


if __name__ == "__main__":
    init_time = time.time()
    time.sleep(2)
    args = sys.argv
    INPUT_FILE = str(args[1])
    results_dict = {}

    n_list = read_file(INPUT_FILE)
    stat_mean = compute_mean(n_list)
    results_dict["mean"] = stat_mean

    stat_mode = compute_mode(n_list)
    results_dict["mode"] = stat_mode

    stat_median = compute_median(n_list)
    results_dict["median"] = stat_median

    stat_std_dev = compute_std(n_list)
    results_dict["std_dev"] = stat_std_dev

    stat_variance = compute_variance(n_list)
    results_dict["variance"] = stat_variance

    end_time = time.time()
    duration = end_time - init_time
    save_data(results_dict, duration)

    print(f"**** Program took {duration} seconds to run ****")
