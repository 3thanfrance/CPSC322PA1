"""
Gina Sprint
CPSC 322-02, Fall 2022
Programming Assignment #1
9/5/2022

Description: This module tests functions in pa1.py
"""

import pa1

# note: order is actual/received student value, expected/solution
def test_remove_missing_values():
    """Unit test for remove_missing_values()

    """
    # missing value is defined as an empty string ""
    header = ["id", "a", "b", "c"]
    table = [["001", "1", "", ""],
             ["002", "", "2", ""]]
    # attempt to remove missing values from a column with no missing values
    cleaned_table = pa1.remove_missing_values(table, header, "id")
    assert cleaned_table == [["001", "1", "", ""],
                             ["002", "", "2", ""]]

    # attempt to remove missing values from a column with one missing value
    cleaned_table = pa1.remove_missing_values(table, header, "a")
    assert cleaned_table == [["001", "1", "", ""]]
    cleaned_table = pa1.remove_missing_values(table, header, "b")
    assert cleaned_table == [["002", "", "2", ""]]

    # attempt to remove missing values from a column with only missing values
    cleaned_table = pa1.remove_missing_values(table, header, "c")
    assert cleaned_table == []
