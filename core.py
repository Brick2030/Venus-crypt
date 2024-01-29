import random

                                # Todo list
# Checking for missing chars before encryption. Maybe changing missing to random.
# Dictionary generator
# Support file systems
# Quick mode? Built in dictionaries?
# Research on input settings


def uniCharList(input): # Return unique symbols in givern line. Used for dictionary and message later.
    uniList = []
    for chr in input:
        if(uniList.count(chr)==0): uniList.append(chr)
        else: continue

    return uniList # Returns array of unique chars


def charIndexList(char, string): # Finds every index of char in string
    indexList = []
    for i, val in enumerate(string):
        if val == char: indexList.append(i)
    
    return indexList

def encrypt(message, dictionary, separator): # Returns encrypted messange
    encryptedMessage = []
    for chr in message:
        thisCharIndexs = charIndexList(chr, dictionary) # All char index in dictionary
        randomIndex = int(random.uniform(0, len(thisCharIndexs))) # Random is float. Converted to int. Maybe better to use math functions before converting.
        encryptedMessage.append(str(thisCharIndexs[int(randomIndex)]))

    return separator.join(encryptedMessage)

def decrypt(key, dictionary, separator): # Decryption
    keyword = key.split(separator)
    decryptedMessage = []
    for number in keyword:
        decryptedMessage.append(dictionary[int(number)])

    return "".join(decryptedMessage)

