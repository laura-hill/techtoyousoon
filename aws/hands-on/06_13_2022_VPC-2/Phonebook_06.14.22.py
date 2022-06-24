from random import randint as ri, choices

def password(name):
    letters = ''.join( choices(name, k=3) ).lower()
    num = str(ri(1000, 9999))
    return letters + num


def main():
    while True:
        name = input("Please enter your full name: ")
        if name.isalpha():
            print(password(name))
            break
        else:
            print("Invalid Entry. Names must not include any spaces, special characters, or numbers.")
            continue
        

if __name__ == "__main__":
    main()