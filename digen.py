import random

Numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

Eng_a_LC = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

Eng_a_UC = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

Spec_Symb = ('\n', '.', ',', ':', ';', '\'', '\"', ' ', '(', ')', '[', ']', '{', '}', '/', '\\')


def gen():
    output = (Numbers + Eng_a_UC + Eng_a_LC + Spec_Symb) * 5
    return "".join(output)

