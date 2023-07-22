#import the required module
from datetime import datetime

#take input from the user
her_dose=int(input("enter hercepten dose: "))
her_pre=int(input("how much do we have? "))
#now we calculate the dose:

if her_dose < her_pre :
    
    ml = round(her_dose/22,2)
    remain = her_pre - her_dose
    print("use {} ml from the old one ".format(ml))
    print("write the remain of herceptin {} mg".format(remain))
    
elif her_dose > her_pre:
    ad = her_dose - her_pre
    calc = round(ad/22)
    remain = 440 - ad
    print("use all of the old one and {} ml from the new one".format(calc))
    print("don't forget to write the remainning herceptin {} mg ".format(remain))
else:
    print("use all of the old one")
now = datetime.now()
current=now.strftime("%I:%M")
day=datetime.today()
current_day=day.strftime("%d/%m/%Y")
print("don't forget to write the day and date")
print(current , current_day)


