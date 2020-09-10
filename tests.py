from main  import *
from fucncs_1 import *
l = ["Si No", "Item Code", "particulars", "QTY" , "MRP", "Batch" , "Exp Date" , "Disc", "Gst Amd", "Total"]

for Variable in rows:
    for Variable1 in Main_bill:
        if Variable[0] == Variable1[0]:
            itemcode = itemcode()
            Si_no = Variable1[0]
            Particulars = Variable[1]
            Quty = Variable1[1]
            Mrp = Variable[3]
            Batch = Variable[6]
            Expdate = Variable[5]
            Discount = Discount_Percent
            Gstamd = Variable[7][:2]
            total = Mrp * Quty + (Mrp * Gstamd) / 100 - (Mrp * Discount_Percent) / 100
            Input = Si_no, itemcode, Particulars, Quty, Mrp, Batch, Expdate, Discount_Percent + "%", (
                        Mrp * Gstamd) / 100, total
            Bill1list.append(Input)
print(tabulate(Bill1list))
