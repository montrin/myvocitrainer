import random
import sys
from termcolor import colored


def test_the_voci(test_voci):
    still_to_learn = []
    for i in random.sample(test_voci, len(test_voci)):
        b = i.split("#")
        question = b[1].replace(b[0],'.......')
        print question

        your_response = raw_input("your try, please ")

        #if it's a gap question
        if '...' in question:
            if your_response == b[0]:
                print b[1].replace(b[0], colored(b[0], 'green'))
            else:        
                print b[1].replace(b[0], colored(b[0], 'yellow'))
                still_to_learn.append(i)
        else:
            if your_response == b[0]:
                print colored(b[0], 'green')
            else:        
                print colored(b[0], 'yellow')
                still_to_learn.append(i)

    return still_to_learn            



with open('voci.txt', 'r') as f:
    data = f.read()

voci_list = data.splitlines()
nr_of_voci = raw_input("How many voci do you want to test?")

try:
    print int(nr_of_voci) < len(voci_list)   
    nr = int(nr_of_voci)
    voci = random.sample(voci_list, nr) if nr < len(voci_list) else random.sample(voci_list, len(voci_list))

except ValueError:
    print "WOoops, entry was not an integer. Try again."


still_to_learn = test_the_voci(voci)
learn_box = []

while(len(still_to_learn) > 0) :
    del learn_box[:]
    learn_box = list(still_to_learn)
    del still_to_learn[:]
    still_to_learn = test_the_voci(learn_box)

    print "Thank you!! Rerun if you want"
    





