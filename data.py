"""
Working with Cancer Data from the 2005 Environmental Protection Agency = Reading, Writing, and Processing Tabular Data 
"""
import csv

def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
    with open(file_name, newline='') as csv_file:
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)
    return csv_table

def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """

    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in csv_table:
            csv_writer.writerow(row)

def select_columns(my_table, col_indices):
    """
    Input: Nested list my_table and a list of integers col_indices
    Output: Nested list corresponding to sub-table formed by
    columns in col_indices
    """
    result = []
    for row in my_table:
        sub_row = [row[index] for index in col_indices]
        answer.append(sub_row)
    return result


def sort_by_column(my_table, col_idx):
    """
    Input: Nested list my_table and an integer col_idx
    Action: Mutate the order of the rows in my_table such that the entries in
    the column col_idx appear in DESCENDING order when interpreted as numbers
    """
    my_table.sort(key = lambda row: float(row[col_idx]), reverse = True)

