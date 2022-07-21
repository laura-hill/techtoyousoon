'''
COMPUTATIONAL THINKING CONCEPTS

ABSTRACTION: We only care about the book's title and the number of copies. We do not
             worry ourselves with other details such as the author or publishing date.

DECOMPOSITION: We decompose the problem by breaking the information into two different
               groups: books with only one copy left and books with more than one copy left

PATTERN RECOGNITION: Pattern recognition is being used by parsing through a list of book names
                     and identifying whether or not a book has already been seen before.

TESTING AND DEBUGGING: After running the code, we are able to view the results and compare
                       against our hypothesis. If the result is different it will allow us
                       to revise our code and debug.

'''


def single_copies(products):
    # By creating this dictionary, I am applying abstraction because
    # we are representing a book by only its title and its count
    inventory = {}
    for product in products:
        # Here I am using pattern recognition by identifying if a
        # book has already been seen before
        if product in inventory:
            inventory[product] += 1
        else:
            inventory[product] = 1
    single_items = []
    for key, value in inventory.items():
        # Here I am applying decomposition by only accepting the data
        # where the count is 1
        if value == 1:
            single_items.append(key)
    for title in single_items:
        print(title)
    
    # LIST COMPREHENSION
    # singles = [key for key, value in inventory.items() if value == 1]
    
    
# Here I applied the testing and debugging foundation by running the code
# and comparing my hypothesis to the result that I received
products = (["Pride and Prejudice", "To Kill a Mockingbird",
                     "The Great Gatsby", "One Hundred Years of Solitude",
                     "Pride and Prejudice", "In Cold Blood",
                     "Wide Sargasso Sea", "One Hundred Years of Solitude",
                     "Brave New World",  "The Great Gatsby", "Brave New World",
                     "I Capture The Castle", "Brave New World", "The Great Gatsby",
                     "The Great Gatsby", "One Hundred Years of Solitude",
                     "Pride and Prejudice"])
single_copies(products)



######################################## TESTING ########################################
'''class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test_single_copies():
    print(f"{bcolors.HEADER}{bcolors.BOLD}{bcolors.UNDERLINE}Testing single_copies(){bcolors.ENDC}")
    try:
        products = []
        observed = single_copies(products)
        assert observed == []
        print(f'{"Accepts an empty list":.<35}{bcolors.OKGREEN}PASSED{bcolors.ENDC}')
    except:
        print(f'{"Accepts an empty list":.<35}{bcolors.FAIL}FAILED{bcolors.ENDC}')

    try:
        products = []
        observed = single_copies(['book1'])
        assert observed == ['book1']
        print(
            f'{"Works on a list of size 1":.<35}{bcolors.OKGREEN}PASSED{bcolors.ENDC}')
    except:
        print(f'{"Works on a list of size 1":.<35}{bcolors.FAIL}FAILED{bcolors.ENDC}')

    try:
        products = ['book1', 'book1']
        observed = single_copies(products)
        assert observed == []
        print(f'{"Detects repeat titles":.<35}{bcolors.OKGREEN}PASSED{bcolors.ENDC}')
    except:
        print(f'{"Detects repeat titles":.<35}{bcolors.FAIL}FAILED{bcolors.ENDC}')

    try:
        products = (["Pride and Prejudice", "To Kill a Mockingbird",
                     "The Great Gatsby", "One Hundred Years of Solitude",
                     "Pride and Prejudice", "In Cold Blood",
                     "Wide Sargasso Sea", "One Hundred Years of Solitude",
                     "Brave New World",  "The Great Gatsby", "Brave New World",
                     "I Capture The Castle", "Brave New World", "The Great Gatsby",
                     "The Great Gatsby", "One Hundred Years of Solitude",
                     "Pride and Prejudice"])
        observed = single_copies(products)
        assert observed == (["To Kill a Mockingbird",
                             "In Cold Blood",
                             "Wide Sargasso Sea",
                             "I Capture The Castle"])
        print(f'{"Works on larger lists":.<35}{bcolors.OKGREEN}PASSED{bcolors.ENDC}')
    except:
        print(f'{"Works on larger lists":.<35}{bcolors.FAIL}FAILED{bcolors.ENDC}')


if __name__ == "__main__":
    test_single_copies()'''