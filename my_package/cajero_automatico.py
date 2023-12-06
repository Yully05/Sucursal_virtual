import random

#variables y matrices
saldo_inicial=250000

usuarios=[]


#funciones


def retirar_cuenta_ahorro(cuenta,monto):
    for nueva_cuenta in cuentas_ahorro:
        if nueva_cuenta["cuenta"] == cuenta:
            if nueva_cuenta["saldo"]>=monto:
                nueva_cuenta["saldo"]-=monto
                print("Retiro realizado exitosamente.")
            else:
                print("Fondos insuficientes.")
        else:
            print("Cuenta no encontrada")

def autenticacion(cuenta):
    for nueva_cuenta in cuentas_ahorro:
        if cuenta==nueva_cuenta["cuenta"]:
            intentos=3
            while intentos>0:
                cedula_ingresada=int(input("Ingrese el numero de cedula para validar titularidad: "))
                if nueva_cuenta["cedula"]==cedula_ingresada:
                    print("Autenticacion exitosa.")
                    break
                else: 
                    print(f"Numero de cedula incorrecto. Tiene {intentos} más: ")
                    intentos-=1
            print("Demasiados intentos fallidos.")  
        else:
            print("Autenticacion fallida. Numero de cedula incorrecto.")          
#llamamos la funcion, ella se encarga de agregar los valores a la lista
  
