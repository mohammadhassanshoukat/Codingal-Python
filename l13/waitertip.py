def total_cal(billamount, tipperc):
    #difine function to calculatte the tip on bill
    total=billamount*(1+0.001*tipperc)
    total=round(total,2)
    print(f"please pay: ${total}")

#specify only bibill amount 
#defualt tip percentage is used 

total_cal(150,20)