#partially based in neetismurder's homework

import random

def ask_yes_or_no( question ):
    '''asks a y/n questions, returns the appropriate boolean'''
    print question,
    response= ""
    while response not in ('y', 'Y', 'n', 'N'):
        response= raw_input()
        if response in ("y", "Y"):
            return True
        elif response in ("n", "N"):
            return False
        else:
            print "Please enter 'y' or 'n'"

def ask_integer( question ):
    '''asks for a integer, returns it'''
    print question,
    while True:
        response= raw_input()
        try:
            return int(response)
        except ValueError:
            print "You must enter a integer!"

def closeness(n1,n2):
    '''evaluates a subjective closeness between two numbers, returns a float in the interval 0..1'''
    MAX_DISTANCE= 50
    n1= float(n1)                       #to make sure we use floating point division
    return 1-min(abs(n1-n2)/MAX_DISTANCE, 1.0)    #truncated rule of three

def map_float_to_list_element(flt, lst):
    '''takes a float f in the interval 0..1 as argument, and maps it into an element from a list. 
    example: map_float_to_list_element(0.2, [5,6])==5   map_float_to_list_element(0.8, [5,6])==6'''
    n= len(lst)
    return lst[ min(n-1, int( flt * n)) ]

def closeness_description(n1, n2):
    '''returns a string describing the closeness between two numbers'''
    STRING_CLOSENESS_DESCRIPTIONS= ("Not in a million years", "Very far", "Far", "Somewhat close", "Close", "Very close", "Almost there!")
    closeness_float= closeness( n1, n2)
    closeness_string= map_float_to_list_element( how_close, STRING_CLOSENESS_DESCRIPTIONS)
    return closeness_string

def play(answer, n_tries):
    '''play the number guessing game'''
    while n_tries>0:
        print "\nYou have", n_tries, "tries left."
        guess= ask_integer("What do you think the number is?")
        if guess!=answer:
            print closeness_description( guess, answer )
            n_tries-=1
        else:
            return "Yes, it's", answer, ". Well done, you had", n_tries, "tries left."
    return "You lose. The number was", answer


floor, ceiling= 0,100
answer = random.randint(floor, ceiling)
do_play= ask_yes_or_no("I'm thinking of a number between {floor} and {ceiling}.\nDo you want to try your luck?".format(**locals()))
print (play(answer, 10) if do_play else "Ok, your call")
