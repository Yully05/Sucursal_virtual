from my_package import accounts,authetication,operations,utils
import pandas as pd
import random

path='my_package/datos.xlsx'
xls = pd.ExcelFile(path)
BD = xls.parse('Hoja1')

bandera_iniciar_sesion = False
user_data = {}
id_usuario=0

print(BD)

def login():
    print("Inicie sesion")
    cedula=int(input("Ingrese su cedula: "))
    bandera_crear_usuario = False
    global user_data
    global id_usuario
    for diccionario_usuario in BD['cedula'].values:    
        cedula_comparar=diccionario_usuario
        if cedula==cedula_comparar:
            user_data = BD[BD['cedula'] == cedula].to_dict(orient='records')[0]
            print(f"Bienvenido {user_data['nombre']}")
            id_usuario=BD.index[BD['cedula'] == cedula].tolist()
            bandera_crear_usuario = False
            break 
        else:
            bandera_crear_usuario = True
    if bandera_crear_usuario:            
        print("El usuario no existe. Debe crear un usuario.")
        nombre=input("Ingrese su nombre completo: ")
        cedula=int(input("Ingrese el numero de cedula: "))
        contraseña=int(input("Asigne una contraseña para su cuenta: "))
        accounts.crear_usuario(nombre,cedula,contraseña)
    

#menu de operaciones  
print("Bienvenido al Cajero BancoVelandia")

while True:
    if not bandera_iniciar_sesion:
        login()   
        bandera_iniciar_sesion = True    
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
                monto=int(input("Digite el monto: "))
                if user_data['saldo_ahorros']-monto>0:
                    print(f"""
    Retiro Exitoso
    por favor retire su dinero
    {monto}
                          """)
                    user_data["saldo_ahorros"]-=monto
                    print(f"su nuevo saldo es: {user_data['saldo_ahorros']}")
                else:
                    print('saldo insuficiente')
   
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
            accounts.actualizar_cuenta(user_data,id_usuario)
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


