import core
import digen

message = input("Enter the message to encrypt:\n")
#message = "Autem numquam maiores et. Iure voluptate enim recusandae cum nihil quisquam. Unde est beatae sint ut dolorum nesciunt. Aut consequatur tenetur"
#message = message.lower()



key = core.encrypt(message, digen.gen(), '.')
print(key)

print('\n')

msg = core.decrypt(key, digen.gen(), '.')
print(msg)
