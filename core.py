import random

                                # Todo list

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



def checkMissing(what, where): # Check if chars in WHAT exist in WHERE. Important.
    missing = [] # List of missing for output
    abort = False # True when any missing - aborts encryption to avoid crashing and outputs missing list. 

    for char in what:
        if (where.count(char) == 0):
            abort = True
            missing.append(char)

    if (abort):
        print("ERROR! Those chars from message are missing in dictionary!")
        print(missing)
        quit()



def encrypt(message, dictionary, separator): # Returns encrypted messange
    
    checkMissing(message, dictionary)

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

