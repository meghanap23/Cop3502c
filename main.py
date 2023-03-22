# Meghana's code
def encode(number):
    encoded_password = ""
    if len(number) == 8: # this if statement ensures that this function works only is input is 8 characters long
        for num in range(len(number)): # for loop used to add 3 to each individual character in input
            encoded_val = int(number[num]) + 3 # user's string input converted to int using int() to facilitate addition
            encoded_password += str(encoded_val)
    return encoded_password # encode() function returns the final encoded password

def menu(): # menu function prints the display menu
    print("Menu")
    print("-------------")
    print("1.Encode")
    print("2.Decode")
    print("3.Quit")

def main():
    run = True # run set to Boolean True for the while loop
    number = 0
    oldNumber = ''locals()

    while run:

        menu() # displays menu
        menu_option = int(input("Please enter an option: ")) # int() converts input to integer
        if menu_option == 1: # if menu choice entered is 1, user's input is encoded
            number = str(input("Please enter your password to encode: "))
            oldNumber = number
            encode(number)
            print("Your password has been encoded and stored!")

        elif menu_option == 2: # when option 2 is selected, the encoded password and the decoded str will be displayed
            print(f"The encoded password is {encode(number)}, and the original password is {oldNumber}.")
        elif menu_option == 3:
            run = False   # run is set to Boolean false so that option 3 exists the while loop

if __name__ == "__main__":
    main()