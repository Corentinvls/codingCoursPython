"""Hello module

Python Docstring
"""


def ascii_to_base_64(string):
    """Convert ascii to base 64
    """
    print("tu a donner " + string)

    input_in_array = string_to_array(string)
    print("1/ ")
    print(input_in_array)

    input_in_ascii = convert_to_ascii(input_in_array)
    print("2/ ")
    print(input_in_ascii)

    input_in_binary = convert_ascii_to_binary(input_in_ascii)
    print("3/ ")
    print(input_in_binary)

    input_in_binary = append_to_start(input_in_binary, 8, "0")
    print("4/ ")
    print(input_in_binary)

    input_in_binary_string = array_to_string(input_in_binary)
    print("5/ ")
    print(input_in_binary_string)

    input_in_byte_array = split_string_at_size(input_in_binary_string, 6)
    print("6/ ")
    print(input_in_byte_array)

    input_in_byte_array_format = append_to_end(input_in_byte_array, 6, "0")
    print("7/ ")
    print(input_in_byte_array_format)

    input_in_decimal_array = convert_binary_to_decimal(input_in_byte_array_format)
    print("8/ ")
    print(input_in_decimal_array)

    input_in_base64_array = decimal_array_to_64(input_in_decimal_array)
    print("9/ ")
    print(input_in_base64_array)

    input_in_base64_string = array_to_string(input_in_base64_array)
    print("10/ ")
    print(input_in_base64_string)

    result = format_to_multiple(input_in_base64_string, 4, "=")
    print("11/ ")
    print(result)
    return result


def base_64_to_ascii(string):
    """Convert base64 to ascii
    """
    print("tu a donner " + string)
    string = remove_useless_char(string, "=")
    base_64_array = string_to_array(string)
    decimal_array=array_base_64_to_decimal(base_64_array)
    print(decimal_array)
    #on convertie en tableau de binaire// ?
    #on convertie en string // array_to_string(array):
    #~on découpe en block de 8 // split_string_at_size(string, 8):
    #~on rempli le dernier par la gauche avec des zeo jusqua ce qu'il fasse 0 ref la ligne d'en dessous//append_to_start(array, 8, "0"):
    #ensuite on converti en ascii // ?
    #et on converti en char // ?
    #puis on converti ce tableau en string // array_to_string(array):
    #on return



def string_to_array(string):
    """exo1 tranform string in array of characters"""
    return list(string)


def array_to_string(array):
    """exo5&10 tranform array to string"""
    return ''.join(array)


def append_to_end(array, length, char_to_add):
    """exo7 & 11 append char to the end of string while string's length inferior at length"""
    for i in range(len(array)):
        array[i] = array[i] + char_to_add * (length - len(array[i]))
    return array


def append_to_start(array, length, char_to_add):
    """exo7 & 11 append char to the start of string while string's length inferior at length"""
    for i in range(len(array)):
        array[i] = char_to_add * (length - len(array[i])) + array[i]
    return array


def format_to_multiple(string, multiple, char_to_add):
    """exo7 & 11 append char to the start of string while string's length inferior at length"""
    while len(string) % multiple != 0:
        string = string + char_to_add
    return string


def decimal_array_to_64(arr):
    """exo9  convert decimal To base64"""
    convert_table = {"0": "A", "16": "Q", "32": "g", "48": "w",
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
        arr[i] = convert_table.get(str(arr[i]))
    return arr


def array_base_64_to_decimal(arr):
    """exo9  convert base64 To decimal"""
    convert_table = {'0': '52', '1': '53', '2': '54', '3': '55',
                     '4': '56', '5': '57', '6': '58', '7': '59',
                     '8': '60', '9': '61', 'A': '0', 'B': '1',
                     'C': '2', 'D': '3', 'E': '4', 'F': '5',
                     'G': '6', 'H': '7', 'I': '8', 'J': '9',
                     'K': '10', 'L': '11', 'M': '12', 'N': '13',
                     'O': '14', 'P': '15', 'Q': '16', 'R': '17',
                     'S': '18', 'T': '19', 'U': '20', 'V': '21',
                     'W': '22', 'X': '23', 'Y': '24', 'Z': '25',
                     'a': '26', 'b': '27', 'c': '28', 'd': '29',
                     'e': '30', 'f': '31', 'g': '32', 'h': '33',
                     'i': '34', 'j': '35', 'k': '36', 'l': '37',
                     'm': '38', 'n': '39', 'o': '40', 'p': '41',
                     'q': '42', 'r': '43', 's': '44', 't': '45',
                     'u': '46', 'v': '47', 'w': '48', 'x': '49',
                     'y': '50', 'z': '51', '+': '62', '/': '63'
                     }
    for i in range(len(arr)):
        arr[i] = convert_table.get(str(arr[i]))
    return arr


binary_table = ['1000001', '1000010', '1000011', '1000100', '1000101']


def convert_ascii_to_binary(array):
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


def convert_binary_to_decimal(numbers_table):
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


def convert_to_ascii(array):
    """exo2 convert each element of array to ASCII """
    for i in range(len(array)):
        array[i] = ord(array[i])
    return array


def split_string_at_size(string, size):
    """exo6 split string at size"""
    return [string[i:i + size] for i in range(0, len(string), size)]


def remove_useless_char(string, char):
    """exo11 delete char from string"""
    return string.replace(char, "")


# input_user = input("Donnez une chaine de caractere : ")
# ascii_to_base_64(input_user)
base_64_to_ascii("QUJDREU=")
