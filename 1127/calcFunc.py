def feeCalc( amt ) :
    fee = 0
    if ( amt <= 200 ) :
        fee = amt * 0.05
    elif ( amt > 400 ) :
        fee = amt * 0.03 + 6
    else :
        fee = amt * 0.04 + 2
    return fee * 1.1