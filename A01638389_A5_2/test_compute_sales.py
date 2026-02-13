"""
Validation script for computeSales.py
"""
import json
import computeSales


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


def test_case1():
    """
    Test Scenario 1
    """
    product_dict = parse_jsonfile(r"tests\TC1\TC1_ProductList.json")
    company_sales = parse_jsonfile(r"tests\TC1\TC1_Sales.json")

    assert computeSales.compute_sales(product_dict, company_sales)[0] == 2481.86


def test_case2():
    """
    Test Scenario 2
    """
    product_dict = parse_jsonfile(r"tests\TC1\TC1_ProductList.json")
    company_sales = parse_jsonfile(r"tests\TC2\TC2.Sales.json")

    assert computeSales.compute_sales(product_dict, company_sales)[0] == 166568.23


def test_case3():
    """
    Test Scenario 3
    """
    product_dict = parse_jsonfile(r"tests\TC1\TC1_ProductList.json")
    company_sales = parse_jsonfile(r"tests\TC3\TC3.Sales.json")
    assert computeSales.compute_sales(product_dict, company_sales)[0] == 165235.37
