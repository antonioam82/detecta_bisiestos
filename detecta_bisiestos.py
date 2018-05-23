from datetime import date
from VALID import opt, ns, OKI #IMPORTAMOS FUNCIONES DE "VALID"
import subprocess

def rang_año():
    while True:
        rang=input("Escriba los años del rango separados por coma: ")
        defe=rang.split(",")
        try:
            co=[int(defe[0]),int(defe[1])]
            co.sort()
        except:
            continue
        if co[0]>=1 and co[1]<=9999:
            return co
            break
        print("RECUERDE QUE EL RANGO HA DE ESTAR ENTRE 1 Y 9999 (AMBOS INCLUIDOS)",chr(7))
    
while True:
    print("DETECTA-BISIESTOS")
    print("¿Que información desea ver?")
    print("A)AÑOS BISIESTOS Y NO BISIESTOS")
    print("B)SOLO AÑOS BISIESTOS")
    print("C)SOLO AÑOS NO BISIESTOS")
    print("D)CONSULTAR UN AÑO")
    op=opt(input("Introduzca aquí su opción: "),["A","B","C","D"])
    if op==("D"):
        año=OKI(input("Indique año: "))
        while año<1 or año>9999:
            año=OKI(input("Año no válido: "))
        if año==9999:
            numdias=365
        else:
            D1=date(año,1,1)
            D2=date(año+1,1,1)
            numdias=(abs(D2-D1).days)
            if numdias==365:
                print("El año",año,"no es bisiesto")
            else:
                print("El año",año,"es bisiesto")
    else:
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
                     numan+=1
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
        if op==("A"):
            print(("Entre %d y %d hay %d años bisiestos")%(rang[0],rang[1],numan))
    conti=ns(input("¿Desa continuar?: "))
    if conti==("n"):
        break
    subprocess.call(["cmd.exe","/C","cls"])
            
