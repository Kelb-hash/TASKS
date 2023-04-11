
 

# List of numbers
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]
list4 = [13, 14, 15, 16]
list5 = [17, 18, 19, 20]
list6 = [21, 22, 23, 24]
list7 = [25, 26, 27, 28]
list8 = [29, 30, 31, 32]
list9 = [33, 34, 35, 36]
list10 = [37, 38, 39, 71]


common = set(list1) & set(list2) or set(list1) & set(list3) or set(list1) & set(list4) or set(list1)\
        & set(list5) or set(list1) & set(list6) or set(list1) & set(list7) or set(list1) & set(list8)\
        or set(list1) & set(list9) or set(list1) & set(list10) or set(list2) & set(list3) or set(list2)\
        & set(list4) or set(list2) & set(list5) or set(list2)& set(list6) or set(list2) & set(list7)\
        or set(list2) & set(list8) or set(list2)& set(list9) or set(list2) & set(list10)\
        or set(list3) & set(list4) or set(list3)& set(list5) or set(list3) & set(list6) or set(list3)& set(list7)\
        or set(list3) & set(list8) or set(list3)& set(list9) or set(list3) & set(list10) or set(list4)& set(list5)\
        or set(list4) & set(list6) or set(list4)& set(list7) or set(list4) & set(list8) or set(list4)& set(list9)\
        or set(list4) & set(list10) or set(list5)& set(list6) or set(list5) & set(list7) or set(list5)& set(list8)\
        or set(list5) & set(list9) or set(list5)& set(list10) or set(list6) & set(list7) or set(list6)& set(list8)\
        or set(list6) & set(list9) or set(list6)& set(list10) or set(list7) & set(list8) or set(list7)& set(list9)\
        or set(list7) & set(list10) or set(list8)& set(list9) or set(list8) & set(list10) or set(list9)& set(list10)



if common:
    print(bool(common))
else:
    print(())
