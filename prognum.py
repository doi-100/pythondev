def Fibo(SecNo):
    a=1
    b=1
    ret =0
    if SecNo == 1:
        return 0
    elif SecNo == 2:
        return 1
    else:
        for i in range(2,SecNo):
            ret = a + b
            a=b
            b=ret
    return ret
