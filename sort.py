"""Hello module

Python Docstring
"""


def sorting(liste):
    """Put zeros at left side
    """

    for i in range(len (liste)):
        mini=i
        for j in range(i+1, len (liste)):
            if liste[j]<liste[mini]:
                mini=j
        liste[i], liste[mini] = liste[mini], liste[i]
    return liste(1000001)
