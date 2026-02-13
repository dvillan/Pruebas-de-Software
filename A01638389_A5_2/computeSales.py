"""
Script for compute the total sales in an specific JSON file
"""
import json
import time
import sys


def compute_sales(catalogue: list, sales: list) -> tuple:
    """
    Computes the total sales from a sales list
    using a specific catalog

    :param catalogue: List of products available
    :type catalogue: list
    :param sales: List of sales parsed
    :type sales: list
    :return: Total sales value and order summary
    :rtype: tuple
    """
    total_sales = 0
    catalogue_map = build_index_map(catalogue)
    shop_list = {}

    for order in sales:
        quantity = int(order["Quantity"])
        # Search product into the index product map
        try:
            price = float(catalogue[catalogue_map[order["Product"]]]["price"])
            total_sales += quantity * price
            shop_list[order["Product"]] = {"Quantity": quantity,
                                           "Price": price,
                                           "Total_price": quantity * price}
            print(f"{quantity} x {order['Product']}    {quantity * price}")
        except KeyError:
            print("Product not found in the catalogue")

    print(f"\nTotal Sales: {round(total_sales,2)}")

    return (round(total_sales, 2), shop_list)


def build_index_map(input_list: list) -> dict:
    """
    In order to improve computation times, indexing
    is made through a product mapping

    :param input_list: Catalogue list of dictionaries
    :type input_list: list
    :return: Product map (Product: Index)
    :rtype: dict
    """
    index_map = {item["title"]: index for index, item in enumerate(input_list)}
    return index_map


def parse_jsonfile(filepath: str):
    """
    Parse a specified JSON file as a python dictionary or list

    :param filepath: Path to JSON file
    :type filepath: str
    :return: Data parsed in form of a python dictionary
    :rtype: dict
    """
    with open(filepath, "r", encoding="utf-8") as file:
        jsonfile = json.load(file)

    return jsonfile


def save_data(input_dict: dict, timestamp: float, sales_t: float):
    """
    Saves data into SalesResult.txt file

    :param input_dict: Order summary
    :type input_dict: dict
    :param timestamp: Time elapsed
    :type timestamp: float
    :param sales_t: Total sales
    :type sales_t: float
    """
    with open('SalesResults.txt', 'w', encoding="utf-8") as new_file:
        new_file.write("Quantity    Product          Price\n")
        for key in input_dict.keys():
            new_file.write(f"{input_dict[key]['Quantity']} x {key}  \
                              {input_dict[key]['Total_price']}\n")
        new_file.write(f"\nTotal Sales: {sales_t}")
        new_file.write(f"\n**** Program took {timestamp} seconds to run ****")


if __name__ == "__main__":
    init_time = time.time()

    args = sys.argv
    INPUT_FILE1 = str(args[1])
    INPUT_FILE2 = str(args[2])

    # Parse JSON files
    product_dict = parse_jsonfile(INPUT_FILE1)
    company_sales = parse_jsonfile(INPUT_FILE2)

    tsales, total_orders = compute_sales(product_dict, company_sales)

    end_time = time.time()
    duration = end_time - init_time
    save_data(total_orders, duration, tsales)

    print(f"**** Program took {duration} seconds to run ****")
