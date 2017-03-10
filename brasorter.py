# write out "what is your name?"
# wait for person to type their input
# copy their input to clipboard 
thispersonsname = raw_input("what is your name? ") 

# print "Hello, their input"
# Tell the user they can type 'b' to add a bra, 's' to add a shirt, 'p' to add pants, or 'WASH' to start the wash
print "\nHello dirty {0}. Thanks for joining us. We see you have some clothes to wash. Let's sort through this shit.".format(thispersonsname)


print "\nIf you have a bra, type 'b'. If you have a shirt, type 's'. If you have pants, type 'p'. Type 'WASH' to start the wash."


# Ask the user what item to put in next and wait for their response.
answer = raw_input("What do you want to do?: ")
number_of_bras = 0
number_of_nonbras = 0



# Until they enter WASH
while answer != 'WASH':
    # if the item is a bra, increase the number_of_bras variable by 1
    if answer == 'b':
        number_of_bras +=1
    # if the item is not a bra, increase the number_of_nonbras variable by 1
    elif answer == 'p' or answer == 's':
        number_of_nonbras +=1
    else:
        print "Sorry, that doesn't mean anything to me."
    answer = raw_input("What do you want to do?: ")

# Once the user enters WASH, start the wash by printing "washing..... washing ....." etc
print "Washing................ washing.............."*6000

# End the wash and tell the user how many items are in the dryer and how many bras are on the rack..
print "\n\n Clothes are washed!"

print "\n You have {0} bras on the rack and {1} non-bras in the dryer.".format(number_of_bras, number_of_nonbras)