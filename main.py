def encode_password(password):
    new = ""
    for char in password:
        encode_char = str((int(char) + 3) % 10)
        new += encode_char
    return new


def decode(password):
    new=""
    for char in password:
        char = str((int(char) - 3) % 10)
        new += char
    return new


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded = encode_password(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            decoded_password = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded_password}.")
            print()

        elif option == "3":
            break

if __name__=="__main__":
    main()

