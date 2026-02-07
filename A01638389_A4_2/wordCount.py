"""
Script that counts the frequency of words in a specified file
"""
import time
import sys

def count_words(input_list: str) -> dict:
    """
    Counts the number of times that words appear into a defined list
    and returns it as a dictionary

    :param input_list: List of words
    :type input_list: str
    :return: Frequency of appereance 
    :rtype: dict
    """
    word_map = {char:0 for char in input_list}

    for word in input_list:
        word_map[word] += 1

    return word_map

def save_data(input_map: dict, timestamp: float):
    """
    Docstring for save_data

    :param input_map: Description
    :type input_map: dict
    """
    with open("WordCountResults.txt", "w", encoding="utf-8") as new_file:
        for key in input_map.keys():
            print(f"{key}    {input_map[key]}")
            new_file.write(f"{key}    {input_map[key]}\n")

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
            content_list.append(line.strip())

    return content_list


if __name__ == "__main__":
    init_time = time.time()

    args = sys.argv
    INPUT_FILE = str(args[1])
    char_list = read_file(INPUT_FILE)

    word_dict = count_words(char_list)

    end_time = time.time()
    duration = end_time - init_time

    save_data(word_dict, duration)
    print(f"**** Program took {duration} seconds to run ****")
