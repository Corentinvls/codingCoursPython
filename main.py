"""Hello module

Python Docstring
"""


def main():
    """The main
    """
    print('hello world')


binary_table = ['1000001', '1000010', '1000011', '1000100', '1000101']
def exo_3(binary_table):
    decimal = 0
    for element in binary_table:
        decimal = decimal * 2 + int(element)
        print(f"The decimal value is: {decimal}")


numbers_table = [16,20,9,3,17,4,20]
def exo_8(numbers_table):
    new_table = []
    for number in numbers_table:
        new_table.append(float(number))
    print(f'number table {new_table}')



if __name__ == '__main__':
    main()

