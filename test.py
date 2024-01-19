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
    message = message.replace(' ', separator)
    words = message.split(separator) # Devide message into words
    encryptedMessage = []

    for word in words:
        for chr in word:
            chr_indexs = charIndexList(chr, dictionary) # All char index in dictionary
            randomIndex = int(random.uniform(0, len(chr_indexs)))
            encryptedMessage.append(str(chr_indexs[int(randomIndex)]))

    return separator.join(encryptedMessage)




def decrypt(key, dictionary, separator): # Decryption
    keyword = key.split(separator)
    decryptedMessage = []
    for number in keyword:
        decryptedMessage.append(dictionary[int(number)])

    return separator.join(decryptedMessage)





# TESTING ####################################################################
#print(uniCharList(message))

key = encrypt("hello hello", dictionary, '-')
print(key)
msg = decrypt(key, dictionary, '-')
print(msg)

#print(Tools.devideIntoWords(message))


# Separators must save spaces

# Checking for missing chars before encryption.