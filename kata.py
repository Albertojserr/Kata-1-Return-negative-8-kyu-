def make_negative( number ):
    if type(number)!=int and type(number)!=float:
        return "No es un número"
    elif number>0.0:
        return -number
    else:
        return number
if __name__=="__main__":
    n=8
    z=-10
    r=0
    m=2.2
    a="a"
    print(make_negative(n))
    print(make_negative(z))
    print(make_negative(r))
    print(make_negative(m))
    print(make_negative(a))