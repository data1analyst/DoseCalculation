#take the desired dose from user:
import datetime
her_dose=int(input("كام الجرعة اللي المفروض نحسبها؟"))
her_pre=int(input(" فمدنا كام بواقي؟ لو معندناش اكتب 0"))
#now we calculate the dose:
calc= her_dose - her_pre
ml = round(calc/22,2)
remain = 440 - calc
print("اسحب الصديمة كلها ومن  الحدسدة اسحب {} مل".format(ml))
print("اكتب على العلبة الباقي {}".format(ramain))
print(" متنساش التاريخ واليوم")
print(datetime.time)


