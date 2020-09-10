import csv
from secrets import *
import time
import random
import math


def itemcode():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    return random_str


with open("MED_LIST.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = []

    for rec in reader:
        rows.append(rec)




def authentication():
    """

    :return: this will return True if the user passes authentication
    """
    username1 = input("Enter your registered name:")
    username = username1.upper()
    if username in userlist:
        password1 = input("Enter the password")
        if password1 == password:
            print("Access Granted!!")
            print(" \n\t\t\t\t\t Welcome to Arsa Pharmacy Management System  \n\n")
            return True
        else:
            print("Incorrect Password")
            return False
    else:
        print("sorry !!. Your not a verified user")
        return False

def serch_by_name(in_,data1):
    """

    :param in_: The input to be searched
    :param data1: The data where the input should be searched
    :return: A list of numbers which is the Si no of medicines that the input matches with
    :return: A dlist of numbers which is the Si no of medicines that the input matches with
    """
    main_l = []
    l2 = []
    for data in in_:
        l2.append(data.upper())

    for a in data1:

        l1 = []
        for b in a[1]:
            l1.append(b.upper())
        if l2 == l1[:len(l2)]:
            main_l.append(a[0])
    if len(main_l) == 0:
        return False
    else:
        return main_l


def search_by_num(list2):


    list1 = []
    for i in rows:
        if i[0] in list2:
            b1 = [i[0], i[1], i[3]]
            list1.append(b1)
    return list1

def Bill_Item_Search(keyword):
    Resultant_list = []
    keyword_list = []
    for i in keyword:
        keyword_list.append(i.upper())
    for medparticular in rows:
        med_search_list = []
        for medname  in medparticular[1]:
            med_search_list.append(medname.upper())
        if keyword_list == med_search_list[:len(keyword_list)]:
            Med_details =medparticular[0],medparticular[1],medparticular[3],medparticular[5]
            Resultant_list.append(Med_details)
    if len(Resultant_list) >= 1:
        return Resultant_list
    else:
        return ["Sorry!! Currently There Are No Medicines That Matches The Keyword Criteria", " ", " ", " "]

print(Bill_Item_Search("sod"))





