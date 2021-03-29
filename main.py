"""Hello module

Python Docstring
"""


def sorting(A):
    for i in range(1, len(A)):
        temporaire = A[i]
        j = i - 1
        while j >= 0 and A[j] > temporaire:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = temporaire
    return A


def main():
    """The main
    """

    print('hello world')
    arr = sorting(list('1000001','1000010','1000011','1000100','1000101'))
    print(arr)


if __name__ == '__main__':
    main()

