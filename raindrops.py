def convert(number):
    number = int(input(""))
    if number mod 3 == 0:
        print "Pling"
    elif number mod 5 == 0:
        print "Plang"
    elif number mod 7 == 0:
        print "Plong"
    else:
        print number
    pass
