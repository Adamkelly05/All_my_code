def daysinmonth():
    def isleap():
        if year % 4 == 0:
            print("28")
        else:
            print("29")

    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))

    if month == 2:
        isleap()

    elif month == 4:
        print("30")

    elif month == 6:
        print("30")

    elif month == 9:
        print("30")
    elif month == 11:
        print("30")
    else:
        print("31")


daysinmonth()
