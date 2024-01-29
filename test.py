import core

message = input("Enter the message to encrypt:\n")
#message = "Autem numquam maiores et. Iure voluptate enim recusandae cum nihil quisquam. Unde est beatae sint ut dolorum nesciunt. Aut consequatur tenetur"
message = message.lower()
dictionary = " abcdefghijklmnopqrstuvwxyz-.abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz-.,()/:;;';labcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz-abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz-abcdefghijklmnopqrstuvwxyz"


key = core.encrypt(message, dictionary, ':')
print(key)
msg = core.decrypt(key, dictionary, ':')
print(msg)
