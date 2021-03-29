"""Hello module

Python Docstring
"""


def main():
    """The main
    """

    arr = stringToArray("blabla")
    print(arr)
    base = decimalTo64([10, 30, 23, 45])
    print(base)
    norm = normalizeString(arr[-1], 6, "0")
    print(norm)
    str = arrayToString(arr)
    print(str)


def stringToArray(string):
    """exo1 tranform string in array of characters"""
    return list(string)


def arrayToString(array):
    """exo5&10 tranform array to string"""
    return ''.join(array)


def normalizeString(string, length, charToAdd):
    """exo7 & 11 append char to the end of string while string's length inferior at length"""
    string = string + charToAdd * (length - len(string))
    return string


def decimalTo64(arr):
    """exo9  convert decimal To base64"""
    convertTable = {"0": "A", "16": "Q", "32": "g", "48": "w",
                    "1": "B", "17": "R", "33": "h", "49": "x",
                    "2": "C", "18": "S", "34": "i", "50": "y",
                    "3": "D", "19": "T", "35": "j", "51": "z",
                    "4": "E", "20": "U", "36": "k", "52": "0",
                    "5": "F", "21": "V", "37": "l", "53": "1",
                    "6": "G", "22": "W", "38": "m", "54": "2",
                    "7": "H", "23": "X", "39": "n", "55": "3",
                    "8": "I", "24": "Y", "40": "o", "56": "4",
                    "9": "J", "25": "Z", "41": "p", "57": "5",
                    "10": "K", "26": "a", "42": "q", "58": "6",
                    "11": "L", "27": "b", "43": "r", "59": "7",
                    "12": "M", "28": "c", "44": "s", "60": "8",
                    "13": "N", "29": "d", "45": "t", "61": "9",
                    "14": "O", "30": "e", "46": "u", "62": "+",
                    "15": "P", "31": "f", "47": "v", "63": "/"}
    for i in range(len(arr)):
        arr[i] = convertTable.get(str(arr[i]))
    return arr


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

