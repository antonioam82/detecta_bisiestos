#DETECTOS DE BISIESTOS SIN HACER USO DE "datetime"
from VALID import opt, ns, OKI
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
        return co
        
    
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
        resto=año%4
        if resto==0:
            print("El año",año,"es bisiesto")
        else:
            print("El año",año,"no es bisiesto")
    else:
        rang=rang_año()
        numan=0
        for i in range(int(rang[0]),(int(rang[1]))+1):
            resto=i%4
            if op==("A"):
                if resto==0:
                     print("El año",i,"es bisiesto")
                     numan+=1
                else:
                    print("El año",i,"no es bisiesto")
            else:
                if op==("B") and resto==0:
                    print(i)
                    numan+=1
                elif op==("C") and numdias!=0:
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
            
