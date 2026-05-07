def Fibo(SecNo):
    if SecNo <=2 :
        return 1 
    else:
        return Fibo(SecNo-1) + Fibo(SecNo-2)
