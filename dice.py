import random

def repeat():
    print "Do you need to roll again?  Y or N?"
    try:
        answer = raw_input(">>> ").lower()
        if answer not in "yn":
            repeat()
        else:
            return answer
    except ValueError:
        repeat()

def read_int(prompt, errmsg, acceptable):
    valid_input = False
    while not valid_input:
        print prompt
        try:
            user_in = int(raw_input(">>> "))
            if user_in not in acceptable:
                print errmsg
            else:
                valid_input = True
        except ValueError:
            print errmsg
    return user_in
    
def dice_throw(number_dice, number_sides):
    """take the results of the user input function and
       roll the specified number of dice with the 
       appropriate number of sides, and return the total"""
    
    max_range = number_dice * number_sides
    return random.randint(1, max_range)

def main():

    prompt = "Please enter the amount of dice you need to throw."
    errmsg = "Please enter a valid amount between 1 and 20!"
    acceptable = range(1,21)
    number_dice = read_int(prompt, errmsg, acceptable)

    prompt = "Please enter the number of sides for each individual die to be thrown."
    errmsg = "Please enter a valid number of sides for regulation dice!"
    acceptable = (3, 4, 6, 8, 10, 12, 20, 100)
    number_sides = read_int(prompt, errmsg, acceptable)

    print  dice_throw(number_dice, number_sides)

    if repeat() == 'y':
        main()
    else:
        print "Adventure Awaits!!!"

if __name__ == '__main__':
    main()
