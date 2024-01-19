#from Tools.py import devideIntoWords
import Tools
import random

#message = input("Enter the message to encrypt:\n")
message = "Autem numquam maiores et. Iure voluptate enim recusandae cum nihil quisquam. Unde est beatae sint ut dolorum nesciunt. Aut consequatur tenetur"
message = message.lower()
dictionary = "abcdefghijklmnopqrstuvwxyz-abcdefghijklmnopqrstuvwxyz"


def uniCharList(input): # Return unique symbols in givern line. Used for dictionary and message later.
    uniList = []
    for chr in input:
        if(uniList.count(chr)==0): uniList.append(chr)
        else: continue

    return uniList # Returns array





def charIndexList(char, string): # Finds every index of char in string
    indexList = []
    
    for i, val in enumerate(string):
        if val == char: indexList.append(i)
    return indexList

def encrypt(message, dictionary, separator): # Returns encrypted messange
    message = message.replace(' ', separator) # ИСПОЛЬЗОВВАТЬ СЕПАРАТОР ФУНКЦИЮ
    words = message.split(separator) # Devide message into words
    encryptedMessage = []

    for word in words:
        for chr in word:
            chr_indexs = charIndexList(chr, dictionary) # All char index in dictionary
            randomIndex = int(random.uniform(0, len(chr_indexs)))
            #print((int(randomIndex)))
            encryptedMessage.append(str(chr_indexs[int(randomIndex)]))

    return "-".join(encryptedMessage)

# TESTING ####################################################################
#print(uniCharList(message))
print(encrypt("hello hello", dictionary, '-'))
#print(Tools.devideIntoWords(message))





# Encrypting each words by changing it by each char to random number from position list
# Deviding each word into char arrays, and assigning to them random index from index array
# Better to have also option for connector chars


# Making uni-char list for dictionary and message (Completed)
# Dividing string array into words (Completed)
# Function that returns all char indexes from the input string (Completed)
# Functions that returns all indexes of a uni-char-list char in input (message)  (completed)

# File separation (completed)
