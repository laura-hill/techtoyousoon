###  This program converts milliseconds into hours, minutes, and seconds ###
def main():
    while True:
        #administrative checks
        choice = input("Please enter the milliseconds (should be greater than 0): ")
        try:
            if choice.isalpha:
                if choice.lower() == 'exit':
                    print('"Exiting the program... Good Bye"')
                    break
            ms = int(choice)
            if ms < 1:
                #The input must be greater than 0
                print('"Not Valid Input !!!"')
                continue
        except:
            #The input must be a positive INTEGER
            print('"Not Valid Input !!!"')
            continue
        #begin with a valid input
        seconds = int((ms/1000)%60)
        mins = int((ms/1000/60)%60)
        hours = int(ms/1000/60/60)
        #The input was not even 1 second
        if ms < 1000:
            print("just {} millisecond/s".format(ms))
            continue
        final_string = ''
        if hours > 0:
            final_string += "{} hour/s ".format(hours)
        if mins > 0:
            final_string += "{} minute/s ".format(mins)
        if seconds > 0:
            final_string += "{} second/s".format(seconds)
        print(final_string)

main()