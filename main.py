# Thomas Neubert
def encode(password):
    password = str(password)
    encoded = ""
    for d in password:
        encoded += str(int(d)+3)
    return encoded


def decode(password):
    password = str(password)
    decoded = ""
    for d in password:
        decoded += str(int(d) - 3)
    return decoded

encodedpassword = ""

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!\n")
        encodedpassword = encode(password)
    elif choice == "2":
        print("The encoded password is " + encodedpassword + ", and the original password is " + decode(encodedpassword) + "\n")
    elif choice == "3":
        break
