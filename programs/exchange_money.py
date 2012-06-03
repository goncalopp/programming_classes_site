ange_rate= 0.764759865
print "How many dollars do you have? ",
dollars=  raw_input()       # get input from user. dollars is a string
dollars = float( dollars )  # dollars is a float now
print "your", dollars, "dollars in EUR:", dollars * exchange_rate
