def consecutive_vowels():
    primed = False
    found = False
    while True:
        word = input("Please enter a string: ")
        if word.isalpha():
            break
        print("Please enter a valid word")
    for letter in word:
        if letter.lower() in ['a','e','i','o','u']:
            if primed:
                found = True
            else:
                primed = True
        else:
            primed = False
    if found:
        print("Positive")
    else:
        print("Negative")
    
if __name__ == "__main__":
    consecutive_vowels()