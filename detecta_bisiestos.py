from datetime import date
from VALID import opt, ns, OKI
import subprocess

def rang_año():
    while True:
        rang=input("Escriba los años del rango separados por coma: ")
        defe=rang.split(",")
        try:
            co=[]
            co.append(int(defe[0]))
            co.append(int(defe[1]))
            co.sort()
        except:
            continue
        if (",") in rang and not (" ") in defe and co[0]>=1 and co[1]<=9999:
            return co
            break
        
    
while True:
    print("DETECTA-BISIESTOS")
    print("¿Que información desea ver?")
    print("A)AÑOS BISIESTOS Y NO BISIESTOS")
    print("B)SOLO AÑOS BISIESTOS")
    print("C)SOLO AÑOS NO BISIESTOS")
    op=opt(input("Introduzca aquí su opción: "),["A","B","C"])
    rang=rang_año()
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
            
