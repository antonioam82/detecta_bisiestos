from datetime import date
from VALID import opt, ns, OKI
import subprocess

def año_val(n):
    while n<1 or n>9999:
        n=OKI(input("Año no válido: "))
    return n
    
while True:
    print("DETECTA-BISIESTOS")
    print("¿Que información desea ver?")
    print("A)AÑOS BISIESTOS Y NO BISIESTOS")
    print("B)SOLO AÑOS BISIESTOS")
    print("C)SOLO AÑOS NO BISIESTOS")
    rang=[]
    op=opt(input("Introduzca aquí su opción: "),["A","B","C"])
    año1=año_val(OKI(input("Primer año del rango: ")))
    rang.append(año1)
    año2=año_val(OKI(input("Segundo año del rango: ")))
    rang.append(año2)
    rang.sort()
    numan=0
    for i in range(int(rang[0]),(int(rang[1]))+1):
        if i==9999:
            numdias=365
        else:
            D1=date(i,1,1)
            D2=date(i+1,1,1)
            numdias=(abs(D2-D1).days)
        if op==("A"):
            if numdias==366:
                print("El año",i,"es bisiesto")
            else:
                print("El año",i,"no es bisiesto")
        else:
            if op==("B") and numdias==366:
                print(i)
                numan+=1
            elif op==("C") and numdias==365:
                print(i)
                numan+=1
    if numan==0 and (op=="B" or op=="C"):
        print("NO HAY AÑOS")
    conti=ns(input("¿Desa continuar?: "))
    if conti==("n"):
        break
    subprocess.call(["cmd.exe","/C","cls"])
            
