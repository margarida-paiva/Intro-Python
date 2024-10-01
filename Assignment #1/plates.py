#Program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s):
        return only_letters(s) or (first2_letters(s) and with_num(s))


#Checks if the plate has between 2 and 6 characters and if is all numbers and letters
def length(s):
    return 2<=len(s)<=6 and s.isalnum()


#Check if the first two characters are letters
def first2_letters(s):
    return s[0:2].isalpha()


#Checks if the plate has only letters
def only_letters(s):
    return s.isalpha()


#Checks if the first number is 0 and theres no letters after numbers
def with_num(s):

    #Keeps the index of the first number
    for i in range(len(s)):
        if s[i].isnumeric():
            ind=i

            #If the first number is not 0, checks if theres no letters after a number
            if s[ind]!="0": #the ind is an integer but s[ind] is a string
                return s[ind::].isnumeric()
            else:
                return False


main()