#a code to give the best hydration labels

while True:

    hyd= int(input('please type in the total hydration needed: '))
    sod = int(input('\nplease enter conc of sod : '))
    vol = int(input('\nper {} ml ?'))
    
    dil= sod / vol 
    
    big = 500
    soln= hyd// 500
    remain= hyd % 500
    if remain < 350 and remain > 100 :
        st=input('\ndo you have 250 ml in stock?').lower()
        if st == 'yes':
            print('\nthen you need {} of {} ml + another {} ml '.format(soln,big, remain))
            print('\neach {} ml contain {} of sodium bicarb'.format(big,big*dil))
            print('\nand the remaining {} ml add {} of sodi'.format(remain,remain*dil))
        elif st == 'no':
            final=remain / soln
            total= final + 500
            print('\nthen you need {} of {} ml'.format(soln,total))
            print('\neach {} contain {} of sodium bicarb '.format(total,dil*total))
    
    elif remain == 0 :
        print('\nyou the need {} of {} ml\nand then add {} of sod for each soln '.format(soln,big,big*dil))
    
    q=input('\ndo you want to try again? ').lower()
    if q == 'no':
        break