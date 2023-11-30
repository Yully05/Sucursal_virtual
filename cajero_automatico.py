import random

#variables y matrices
saldo_inicial=250000

usuarios=[]


#funciones
def crear_usuario(nombre,cedula,contraseña):
    nueva_cuenta={"nombre":nombre,
                  "cedula":cedula,
                  "contraseña":contraseña
                  }
    usuarios.append(nueva_cuenta)

def crear_cuenta_ahorro(cuenta_ahorros,saldo_ahorros):
    nueva_cuenta={"cuenta_ahorros":cuenta_ahorros, 
                  "saldo_cuenta_ahorros":saldo_ahorros,
                  }
    usuarios.append(nueva_cuenta)

def crear_cuenta_corriente():
    pass

def crear_tarjeta_credito():
    pass

def eliminar_cuenta_ahorro():
    pass

def eliminar_cuenta_corriente():
    pass

def eliminar_tarjeta_credito():
    pass

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
crear_usuario("juan",1116280179,1234)    
#menu de operaciones  
print("Bienvenido al Cajero Multifuncional")

while True:
    print("Inicie sesion")
    cedula=int(input("Ingrese su cedula: "))
    bandera_crear_usuario = False
    for diccionario_usuario in usuarios:    
        cedula_comparar=diccionario_usuario.get('cedula')
        if cedula==cedula_comparar:
            print(f"Bienvenido {diccionario_usuario['nombre']}")
            id_usuario=print(usuarios.index(diccionario_usuario))
            bandera_crear_usuario = False
            break 
        else:
            bandera_crear_usuario = True
    if bandera_crear_usuario:            
        print("El usuario no existe. Debe crear un usuario.")
        nombre=input("Ingrese su nombre completo: ")
        cedula=int(input("Ingrese el numero de cedula: "))
        contraseña=int(input("Asigne una contraseña para su cuenta: "))
        crear_usuario(nombre,cedula,contraseña)       
    print("___Menu principal___")
    print("""
    ¿Qué operacion desea realizar?
    1. Retirar dinero
    2. Consignar dinero
    3. Pagar una factura de servicio publico
    4. Crear, eliminar o buscar una cuenta
    0. Salir
    """)
    opcion=input("Seleccione una opcion: ")

    if opcion=="1":
        while True:  
            print("""
                1. Retirar dinero de una cuenta de ahorros
                2. Retirar dinero de una tarjeta de credito
                3. Retirar giro nacional
                4. Retirar giro internacional
                0. Volver al menu anterior
                """)
            opcion=input("Seleccione una opcion: ") 
            if opcion=="1": #retirar cuenta ahorro
                cuenta=int(input("Digite su numero de cuenta: "))
                monto=float(input("Digite el monto: "))
                autenticacion()
                retirar_cuenta_ahorro(cuenta,monto)
   
                
            elif opcion=="2":
                pass
            elif opcion=="3":
                pass
            elif opcion=="4":
                pass
            elif opcion=="0":
                break
            else:
                print("Opcion invalida. Intente nuevamente: ")

    elif opcion=="2":
        while True:  
            print("""
    1. Consignar dinero a una cuenta de ahorros
    2. Consignar dinero de una cuenta corriente
    3. Consignar un giro nacional
    4. Consignar un giro internacional
    0. Volver al menu anterior
    """)
            opcion=input("Seleccione una opcion: ") 
            if opcion=="1": #consignar cuenta ahorro
                pass
            elif opcion=="2":
                pass
            elif opcion=="3":
                pass
            elif opcion=="4":
                pass
            elif opcion=="0":
                break
            else:
                print("Opcion invalida. Intente nuevamente: ")
    elif opcion=="3":
        while True:  
            print("""
                1. Servicio de energía
                2. Servicio de agua
                3. Servicio de gas natural
                0. Volver al menu anterior
                """)
            opcion=input("Seleccione una opcion: ") 
            if opcion=="1":
                pass
            elif opcion=="2":
                pass
            elif opcion=="3":
                pass
            elif opcion=="0":
                break
            else:
                print("Opcion invalida. Intente nuevamente: ")
    elif opcion=="4": 
        while True:  
            print("""
        1. Crear una cuenta 
        2. Eliminar una cuenta 
        3. Buscar una cuenta 
        0. Volver al menu anterior
        """)
            opcion=input("Seleccione una opcion: ") 
            if opcion=="1": #crear cuenta
                while True:  
                    print("""
                1. Cuenta de ahorros
                2. Cuenta corriente
                3. Tarjeta de credito
                0. Volver al menu anterior
                """)
                    opcion=input("Seleccione una opcion: ") 
                    if opcion=="1": #crear cuenta ahorros
                        cuenta_ahorros=random.randint(10**9, 10**10-1) #numero aleatorio de 10 dígitos
                        
                        crear_cuenta_ahorro(cuenta_ahorros,saldo_ahorros)
                
                
                
                
                    saldo=int(input("Debe consignar para que su cuenta sea activada: "))
                    numero_cuenta=random.randint(10**9, 10**10-1) #numero aleatorio de 10 dígitos
                    contraseña=int(input("Asigne una contraseña para su cuenta: "))
                    crear_cuenta_ahorro(nombre,cedula,saldo,numero_cuenta,contraseña)
                    print(f"Cuenta de ahorros creada exitosamente. El numero de cuenta es: {numero_cuenta}")
            elif opcion=="2":
                pass
            elif opcion=="3":
                pass
            elif opcion=="0":
                break
            else:
                print("Opcion invalida. Intente nuevamente: ")
    elif opcion=="0":
        print("Gracias por utilizar nuestros servicios.")
        exit()
    else:
        print("Opcion invalida. Intente nuevamente: ")

