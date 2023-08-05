print("Hello Dr.")

#drugs dictionaries
drugs={"cytarabine":[100,5],"oncovin":[1,1],"adriamycin":[50,25],"taxoter":[80,8],"carboplatin":[450,45],"taxol":[100,16.67]}

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
                    print("please dilute {:.2f} ml ".format(final_dilu))
                else:    
                    print("please dilute {:.2f} ml equal to {} vials of {} + {} ml ".format(final_dilu,round(n_vial,2),drug_name,round(remain,2)))

    elif drug_name != drug:
        print("the drug hasn't been updated yet")
        print("you can check your drugs available in this list:")
        print(list(drugs.keys()))
    
    q = input("do you want to try again?")
    if q == "no":
        break                          
