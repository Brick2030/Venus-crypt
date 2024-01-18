#message = input("Enter the message to encrypt:\n")
message = "Autem numquam maiores et. Iure voluptate enim recusandae cum nihil quisquam. Unde est beatae sint ut dolorum nesciunt. Aut consequatur tenetur"
message = message.lower()
dictionary = "abcdefghijklmnopqrstuvwxyz"


def uniCharList(input): # Return unique symbols in givern line. Used for dictionary and message later.
    uniList = []
    for chr in input:
        if(uniList.count(chr)==0): uniList.append(chr)
        else: continue

    return uniList # Returns array

def devideIntoWords(input): # Splits (input) into word list
    return input.split()



def charIndexList(char, string): # Finds every index of char in string
    indexList = []
    
    for i, val in enumerate(string):
        if val == char: indexList.append(i)
    return indexList

# TESTING ####################################################################
#print(uniCharList(message))
print(charIndexList('a', message))




# Functions that returns all indexes of a uni-char-list char in input (message)  


# Encrypting each words by changing it by each char to random number from position list
# Deviding each word into char arrays, and assigning to them random index from index array
# Better to have also option for connector chars


# Making uni-char list for dictionary and message (Completed)
# Dividing string array into words (Completed)
# Function that returns all char indexes from the input string (Completed)
