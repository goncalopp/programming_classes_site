secret_number= 3
user_number= -1

while (secret_number!=user_number):
    print "guess my secret number between 1 and 10! : ",
    user_number= int(raw_input())
    if user_number==secret_number:
        print "you win!"
    else:
        print "no, it's not", user_number

