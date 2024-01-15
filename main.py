#! /usr/bin/python3
########################################################################
#title: name_kana_random_generator
#description: create random Japanese name data in csv format
########################################################################
import csv
import random

def get_random_row(csv_file_path, has_header=True):
    """
    Get a randomly selected row from a CSV file.

    Parameters:
    - csv_file_path (str): Path to the CSV file.
    - has_header (bool): True if the CSV file has a header, False otherwise.

    Returns:
    - list: A list representing the randomly selected row.
    """
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        if has_header:
            header = next(csv_reader)  # Read the header row
        data_rows = list(csv_reader)

    # Count the number of rows
    num_rows = len(data_rows)

    # Check if there are rows in the CSV
    if num_rows > 0:
        # Generate a random number within the range of the row count
        random_number = random.randint(1, num_rows)

        # Access the row using the random number
        random_row = data_rows[random_number - 1]  # Adjust index for 0-based list

        return random_row
    else:
        return None

def join_random_rows(csv_file_path1, csv_file_path2, has_header=True):
    """
    Get randomly selected rows from two different CSV files and join the results.

    Parameters:
    - csv_file_path1 (str): Path to the first CSV file.
    - csv_file_path2 (str): Path to the second CSV file.
    - has_header (bool): True if the CSV files have a header, False otherwise.

    Returns:
    - list: A list representing the concatenated values of the randomly selected rows from both CSV files.
    """
    random_row1 = get_random_row(csv_file_path1, has_header)
    random_row2 = get_random_row(csv_file_path2, has_header)

    if random_row1 and random_row2:
        return random_row1 + random_row2
    else:
        return None

# Example usage:
csv_file_path1 = '/content/name_kana_sample/data1.csv'  # LAST_NAME  : [last_name, kana]
csv_file_path2 = '/content/name_kana_sample/data1.csv'  # FIRST_NAME : [first_name, kana, gender]
header_present = False # Set to True if the CSV files have headers, False otherwise

result = join_random_rows(csv_file_path1, csv_file_path2, header_present)

if result:
    print(f"Result of join_random_rows: {result}")
else:
    print("CSV file(s) is/are empty.")
