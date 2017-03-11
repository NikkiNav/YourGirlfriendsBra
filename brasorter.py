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
items = []


# Until they enter WASH
while answer != 'WASH':
    # if the item is a bra, increase the number_of_bras variable by 1
    if answer == 'b':
        number_of_bras +=1
        items.append('bra')
        print "\n\n\n\nAdded a bra to the washer.\n\n\n\n"
    # if the item is not a bra, increase the number_of_nonbras variable by 1
    elif answer == 'p':
        number_of_nonbras +=1
        items.append('pants')
        print "\n\n\n\nOne more pair of pants in the washer.\n\n\n\n"
    elif answer == 's':
        number_of_nonbras +=1
        items.append('shirt')
        print "\n\n\n\nAdded a shirt to the washer.\n\n\n\n"
    else:
        print "\n\n\n\nSorry, that doesn't mean anything to me.\n\n\n\n"
    answer = raw_input("What do you want to do?: ")

# Once the user enters WASH, start the wash by printing "washing..... washing ....." etc
print "Washing................ washing.............."*6000

# End the wash and tell the user how many items are in the dryer and how many bras are on the rack..
print "\n\nClothes are washed!"


# =======================
# Version 2 begins here
# =======================
print "\nYou have {0} bras (some yours, some hers), and {1} non-bras in the laundry.".format(number_of_bras, number_of_nonbras)

print "\nTime to sort! Don't fuck this up!"
print "\nYou get a point for every item of clothing put in an even slightly acceptable place. If you destroy a bra, you lose a point. If you drop something on the floor, your points stay the same."

score = 0

for item in items:

    if item == 'pants':
        response = raw_input("\nWhat should we do with these {0}? Type 'd' to put it in the dryer and 'r' to hang it on the rack. ".format(item))        
    else:
        response = raw_input("\nWhat should we do with this {0}? Type 'd' to put it in the dryer and 'r' to hang it on the rack. ".format(item))


    if item == 'bra':
        if response == 'r':
            print '\n\n\n\nPhew. Yes. On the rack.\n\n\n'
            score += 1
        elif response == 'd':
            print "\n\n\n\nNooooOOOOOO. That loses you points!\n\n\n"
            score -= 1
        else:
            print "\n\n\n\nNice. It's on the floor.\n\n\n"
    else:
        if response == 'r':
            print "\n\n\n\nIt's on the rack. That'll work.\n\n\n"
            score += 1
        elif response == 'd':
            print "\n\n\n\nIt's in the dryer. Cool.\n\n\n"
            score += 1
        else:
            print "\n\n\n\nNice. It's on the floor.\n\n\n"


percentage = 100*(float(score)/float(len(items)))

if percentage >= 85:
    print "\nAll done! You scored {0} for {1} items of clothing. That's {2} percent. Dope.".format(score, len(items), percentage)    
elif 45 < percentage < 85:
    print "\nAll done! You scored {0} for {1} items of clothing. That's {2} percent. Meh.".format(score, len(items), percentage)
else:
    print "\nAll done! You scored {0} for {1} items of clothing. That's {2} percent. And that sucks. For the bra and yall's relationship.".format(score, len(items), percentage)