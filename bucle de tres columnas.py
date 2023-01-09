#como hacer un bucle de tres columnas q no se repita?
a,b,c= 0,0,0
while a<3:
    while b<3:
        while c<3:
            print(a,b,c)
            c+=1
        b+=1
        c=0
    a+=1
    b=0
    c=0
