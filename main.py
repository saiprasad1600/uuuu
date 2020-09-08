from fucncs_1 import *
from secrets import *

Entry = authentication()

if Entry:
    print('''1.\tSearch For Medicines\n2.\tCreate Bill\n''')
    Option = int(input("Enter The Option\n:"))
    if Option == 1:
        a = input("Enter the Keyword to search\n:")
        op1_list = serch_by_name(a,rows)
        if op1_list is False:
            print("Currently there is no Medicine that matches keyword {}".format(a))
        else:
            else_out = search_by_num(op1_list)
            print("the following Medicines meet the keyword")
            for i in else_out:
                print(i[0],i[1])
    elif Option == 2:
        i = True
        while i == True:
            Name = input("Enter Med Name")
            if Name.upper() == "EXIT":
                i = False
            else:















