#import the required module
from datetime import datetime

her_dose=int(input("enter hercepten dose: "))
her_pre=int(input("how much do we have? "))
#now we calculate the dose:

calc= her_dose - her_pre
if her_dose < 440:
    ml = round(calc/22,2)
    remain = 440 -calc
    print("use all of the old one and {} ml from the new one".format(ml))
    print("write the remain of herceptin {}mg".format(remain))
    
elif her_dose > 440:
    ad= her_dose - 440 
    if ad > her_pre:
        re= ad-her_pre
        print("use the old and new vials and you stil need {}mg equal to {} ml".format(re, round(re/22,2)))
    else:
        print("use the whole new one and take {} ml form the old one".format(ad))
now = datetime.now()
current=now.strftime("%I:%M")
day=datetime.today()
current_day=day.strftime("%d/%m/%Y")
print("don't forget to write the day and date")
print(current , current_day)


