while True:

    fl_conc=int(input("What's the conc. of 5-Flu ? "))
    hrs=int(input("For how much hours to pump? "))
    dl=(hrs*2)-(fl_conc/50)
    if dl > 0:
        print("you should add {} ml of the diluent".format(dl))
    else:
        print("pump will last more than {} without dilution".format(hrs))
    ask=input("do you want to try again? ")
    if ask == "no":
        break
