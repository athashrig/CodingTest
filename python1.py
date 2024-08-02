import csv

def read_csv_file(file_name):
    """
    Reads a CSV file and displays its contents.

    Args:
        file_name (str): The name of the CSV file to read.

    Returns:
        None
    """
    try:
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_csv_file('Athashri.csv')

#OUTPUT
#['1', '20']
#['2', '19']
#['3', '18']
#['4', '17']
#['5', '16']
#['6', '15']
#['7', '14']
#['8', '13']
#['9', '12']
#['10', '11']
#['11', '10']
#['12', '9']
#['13', '8']
#['14', '7']
#['15', '6']
#['16', '5']
#['17', '4']
#['18', '3']
#['19', '2']
#['20', '1']
