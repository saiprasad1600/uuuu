from fucncs_1 import *
from tabulate import tabulate

Entry = authentication()

if Entry:
    print('''1.\tSearch For Medicines\n2.\tCreate Bill\n''')
    Option = int(input("Enter The Option\n:"))
    if Option == 1:
        a = input("Enter the Keyword to search\n:")
        op1_list = serch_by_name(a, rows)
        if op1_list is False:
            print("Currently there is no Medicine that matches keyword {}".format(a))
        else:
            else_out = search_by_num(op1_list)
            print("the following Medicines meet the keyword")
            for i in else_out:
                print(i[0], i[1])
    elif Option == 2:
        i = True
        Main_bill = []
        while i:
            Keyword = input("Enter The Keyword")
            if Keyword.upper() != "EXIT":
                keywordsearch = Bill_Item_Search(Keyword)
                print(tabulate(keywordsearch))
                Med_Number = int(input("Enter The Medicine Code"))
                Quantity = int(input("Enter The Quantity Required"))
                values = [Med_Number, Quantity]
                Main_bill.append(values)
            else:
                i = False
        if i == False:
            Discount = input("Do you Want to Give any discount")
            if Discount.upper() == "YES":
                Discount_Percent = float(input("Enter the Discount Percentage"))
            else:
                Discount_Percent = 0.0
            Bill1list = [
                ["SiNo", "Item Code", "particulars", "QTY", "MRP", "Batch", "Exp Date", "Discount%", "Gst Amound", "Total"]]
            for Variable in rows:
                for Variable1 in Main_bill:
                    if int(Variable[0])== Variable1[0]:
                        Itemcode = itemcode()
                        Si_no = int(Variable1[0])
                        Particulars = Variable[1]
                        Quty = int(Variable1[1])
                        Mrp = float(Variable[3][1:])
                        Batch = Variable[6]
                        Expdate = Variable[5]
                        Discount = Discount_Percent
                        Gstamd = float(Variable[7][:2])
                        total = Mrp * Quty + (Mrp * Gstamd) / 100 - (Mrp * Discount_Percent) / 100
                        Input = [Si_no, Itemcode
                            , Particulars, Quty, Mrp, Batch, Expdate, Discount_Percent, (Mrp * Gstamd) / 100, total]
                        Bill1list.append(Input)

            print(tabulate(Bill1list))

