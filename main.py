"""Hello module

Python Docstring
"""


def main():
    """The main
    """
    print('hello world')


def exo2():
    mytab = [65, 66, 67, 68, 69]
    for i in mytab:
        print(chr(i))


def exo6():
    mylist = '0100000101000010010000110100010001000101'
    # for i in mylist.split():
    #     print(list(i))
    length = len(mylist)
    split = length//6
    result = mylist[:split]
    print(result)


if __name__ == '__main__':
    exo6()
