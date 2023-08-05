#a code to calculate methotrexate dose:
print("Hello Dr.")
drugs={"cytarabine":[100,5],"oncovin":[1,1],"adriamycin":[50,25],"taxoter":[80,8],"carboplatin":[450,45]}

drugs["platinol"]=[50,50]
drugs["methotrexate"]=[500,20]
drugs["dactinomycin"]=[0.5,1]
while True:
#take input from the user
    drug_name=input("please input drug name: ").lower()
    if drug_name in drugs.keys():
        drug_con=float(input("please enter conc needed: "))

    for drug, vial in drugs.items():
        if drug_name==drug:
            final_dilu=drug_con/(vial[0]/vial[1])
            n_vial=final_dilu//vial[1]
            remain=final_dilu%vial[1]
            if n_vial == 0 or remain == 0 :
                print("please dilue {} ml ".format(final_dilu))
            else:    
                print("please dilue {} ml equal to {} vials of {} + {} ml ".format(final_dilu,round(n_vial,2),drug_name,round(remain,2)))
        else:
            print("the drug hasn't been updated yet")
            print("you can check your drugs available in this list:")
            print(list(drugs.keys()))
    w=input("do you want to try again?")
    if w == "no":
        break
        
    
