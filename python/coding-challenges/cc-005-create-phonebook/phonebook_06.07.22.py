def find_number(book, name):
    print(book[name] + '\n')
    
def delete_number(book, name):
    del book[name]
    
def add_number(book, name, num):
    book[name] = num
    
def main():
    phonebook = {}
    menu = '1. Find phone number\n2. Insert a phone number\n3. Delete a person from the phonebook\n4. Terminate'
    print('Welcome to the Phonebook Application')
    while True:
        print(menu)
        choice = input('Select operation on Phonebook App (1/2/3/4) : ')
        if choice not in ['1', '2','3','4']:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue
        if choice == '1':
            while True:
                name = input("Insert name of the person : ")
                if all(x.isalpha() or x.isspace() for x in name):
                    try:
                        find_number(phonebook, name)
                        break
                    except:
                        print("That contact was not found")
                        tryAgain = input("Do you wish to try again? (y/n) : ")
                        if tryAgain.lower() == 'y':
                            continue
                        else:
                            break
                else:
                    print("Please enter a valid name")
                    tryAgain = input("Do you wish to try again? (y/n) : ")
                    if tryAgain.lower() == 'y':
                        continue
                    else:
                        break
        if choice == '2':
            while True:
                name = input("Insert name of the person : ")
                if all(x.isalpha() or x.isspace() for x in name):
                    while True:
                        num = input("Insert phone number of the person : ")
                        if num.isdigit() and len(num) == 10:
                            try:
                                add_number(phonebook, name, num)
                                print(f'Phone number of {name} is inserted into the phonebook\n')
                                break
                            except:
                                print("That number could not be added")
                                tryAgain = input("Do you wish to try again? (y/n) : ")
                                if tryAgain.lower() == 'y':
                                    continue
                                else:
                                    break
                        else:
                            print("Please enter a valid number that is 10 digits long with no special characters")
                            tryAgain = input("Do you wish to try again? (y/n) : ")
                            if tryAgain.lower() == 'y':
                                continue
                            else:
                                break
                else:
                    print("Please enter a valid name")
                    tryAgain = input("Do you wish to try again? (y/n) : ")
                    if tryAgain.lower() == 'y':
                        continue
                    else:
                        break
                break
        if choice == '3':
            while True:
                name = input("Insert name of the person : ")
                if all(x.isalpha() or x.isspace() for x in name):
                    yesNo = input("Are you sure you would like to delete this contact? (y/n) : ")
                    if yesNo.lower() == 'y':
                        try:
                            delete_number(phonebook, name)
                            print(f'{name} is deleted from the phonebook\n')
                            break
                        except:
                            print("The contact that you are trying to delete does not exist in the phonebook")
                            tryAgain = input("Do you wish to continue? (y/n)")
                            if tryAgain.lower() == 'y':
                                continue
                            else:
                                break
                    else:
                        tryAgain = input("Do you wish to enter a different name? (y/n) : ")
                        if tryAgain.lower() == 'y':
                            continue
                        else:
                            break
                else:
                    print("Please enter a valid name")
                    tryAgain = input("Do you wish to try again? (y/n) : ")
                    if tryAgain.lower() == 'y':
                        continue
                    else:
                        break
        if choice == '4':
            print('Exiting Phonebook')
            break
        
if __name__ == "__main__":
    main()