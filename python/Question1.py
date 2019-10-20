# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    debt=initialLevelOfDebt
    rp=repaymentPercentage
    ip=interestPercentage
    repay=(debt*rp)/100
    initdebt=debt
    count=0
    while debt>50:
        debt=debt*(1+ip/100)-repay
        count+=1

    final=count*repay+0.1*initdebt+debt
    answer =int(final)
    return answer
