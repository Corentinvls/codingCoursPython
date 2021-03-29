"""Hello module

Python Docstring
"""


def convert_base_64(inputUser):
    """The main
    """

    print("tu a donner " + inputUser)

    inputInArray = string_to_array(inputUser)
    print("1/ ")
    print(inputInArray)

    inputInASCII = convertToASCII(inputInArray)
    print("2/ ")
    print(inputInASCII)

    inputInBinary = convertASCIItoBinary(inputInASCII)
    print("3/ ")
    print(inputInBinary)

    inputInBinary = appendToStart(inputInBinary, 8, "0")
    print("4/ ")
    print(inputInBinary)

    inputInBinaryString = arrayToString(inputInBinary)
    print("5/ ")
    print(inputInBinaryString)

    inputInByteArray = splitStringAtSize(inputInBinaryString, 6)
    print("6/ ")
    print(inputInByteArray)

    inputInByteArrayFormat = appendToEnd(inputInByteArray, 6, "0")
    print("7/ ")
    print(inputInByteArrayFormat)

    inputInDecimalArray = convertBinaryToDecimal(inputInByteArrayFormat)
    print("8/ ")
    print(inputInDecimalArray)

    inputInBase64Array = decimalArrayTo64(inputInDecimalArray)
    print("9/ ")
    print(inputInBase64Array)

    inputInBase64String = arrayToString(inputInBase64Array)
    print("10/ ")
    print(inputInBase64String)

    result = formatToMultiple(inputInBase64String, 4, "=")
    print("11/ ")
    print(result)
    return result


def string_to_array(string):
    """exo1 tranform string in array of characters"""
    return list(string)


def arrayToString(array):
    """exo5&10 tranform array to string"""
    return ''.join(array)


def appendToEnd(array, length, charToAdd):
    """exo7 & 11 append char to the end of string while string's length inferior at length"""
    for i in range(len(array)):
        array[i] = array[i] + charToAdd * (length - len(array[i]))
    return array


def appendToStart(array, length, charToAdd):
    """exo7 & 11 append char to the start of string while string's length inferior at length"""
    for i in range(len(array)):
        array[i] = charToAdd * (length - len(array[i])) + array[i]
    return array


def formatToMultiple(string, multiple, charToAdd):
    """exo7 & 11 append char to the start of string while string's length inferior at length"""
    while len(string) % multiple != 0:
        string = string + charToAdd
    return string


def decimalArrayTo64(arr):
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


def convertASCIItoBinary(array):
    """exo3 TODO fix ça """
    for i in range(len(array)):
        binary = bin(array[i])
        array[i] = "".join(binary[2:])
    return array


numbers_table = [16, 20, 9, 3, 17, 4, 20]


def sorting(array):
    """exo bonus"""
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


def convertBinaryToDecimal(numbers_table):
    """exo8  convert binary element of an array to decimal """
    decimale_table = []
    for binary in numbers_table:
        int_val, i, n = 0, 0, 0
        while (binary != 0):
            a = int(binary) % 10
            int_val = int_val + a * pow(2, i)
            binary = int(binary) // 10
            i += 1
        decimale_table.append(int_val)
    return decimale_table


def convertToASCII(array):
    """exo2 convert each element of array to ASCII """
    for i in range(len(array)):
        array[i] = ord(array[i])
    return array


def splitStringAtSize(string, size):
    return [string[i:i + size] for i in range(0, len(string), size)]


if __name__ == '__main__':
    convert_base_64("ABCDE")
