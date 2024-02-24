import core
import digen

while(True):
    choice = input("\n1) Encrypt:\n2) Decrypt:\n3) Exit:\n")
    match choice:
        case "1":
            message = input("Enter the message to encrypt:\n")
            key = core.encrypt(message, digen.gen(), '.')
            print(key)
        case "2":
            key = input("Enter key to decrypt:\n")
            msg = core.decrypt(key, digen.gen(), '.')
            print(msg)
        case "3":
            quit()

        case _:
            print("Try again!\n")



