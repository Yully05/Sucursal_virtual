from my_package import accounts,authetication,operations,utils,cajero_automatico
import pandas as pd
import random
import getpass

path='my_package/datos.xlsx'
xls = pd.ExcelFile(path)
BD = xls.parse('users')

user_data = {}
id_usuario=0

cajero_automatico.cantidad_dinero()

def login():
    print("Inicie sesion")
    cedula=int(input("Ingrese su cedula: "))
    global user_data
    global id_usuario
    for diccionario_usuario in BD['cedula'].values:    
        cedula_comparar=diccionario_usuario
        if cedula==cedula_comparar:
            user_data = BD[BD['cedula'] == cedula].to_dict(orient='records')[0]
            print(f"Bienvenido {user_data['nombre']}")
            id_usuario=BD.index[BD['cedula'] == cedula].tolist()
            return 1
    else:            
        print("El usuario no existe, Desea crear un usuario? Y/N: ")
        opc = input()
        if opc == 'y' or opc == 'Y': 
            nombre=input("Ingrese su nombre completo: ")
            cedula=int(input("Ingrese el numero de cedula: "))
            contraseña=int(input("Asigne una contraseña para su cuenta: "))
            accounts.crear_usuario(nombre,cedula,contraseña)
            return 1
        else:
            return 0    
        
def retirar_dinero(cuenta):
    #retirar cuenta ahorro
    contraseña = getpass.getpass("Ingresa tu contraseña: ")
    if contraseña==str(user_data['contraseña']):
        monto=int(input("Digite el monto: "))
        if user_data[cuenta]-monto>=0 and monto % 10000==0:
            print(f"""Retiro Exitoso, por favor retire su dinero ${monto}""")
            print(f'se cobra impuesto 4x1000 por {monto*4/1000}')
            #aqui se va a poner que cobre 10k a la t c
            user_data[cuenta]-=(monto + monto*4/1000)
            cajero_automatico.entregar_dinero(monto)
            print(f"su nuevo saldo es: ${user_data[cuenta]}")
        elif monto % 10000 == 0:
            print('saldo insuficiente')
        else:
            print('Monto incorrecto')
    else:
            print('Clave incorrecta')
def consignar(cuenta,tipo):
    cantidad=int(input('digite la cantidad a consignar'))
    numero_cuenta=int(input('digite el numero de cuenta'))
    for diccionario_usuario in BD[cuenta].values:    
        cuenta_comparar=diccionario_usuario
        if numero_cuenta==cuenta_comparar:
            user_data = BD[BD[cuenta] == numero_cuenta].to_dict(orient='records')[0]
            user_data[tipo]+=cantidad
            print(f"Consignando dinero ... a {user_data['nombre']}")
            id_usuario=BD.index[BD[cuenta] == numero_cuenta].tolist()
            print(f"Consignacion exitosa por {cantidad}")
    accounts.actualizar_cuenta(user_data,id_usuario)
        
    
    
                   
def menu_principal():
    print("___Menu principal___")
    print("""
    Qué operacion desea realizar?
    1. Retirar dinero
    2. Consignar dinero
    3. Pagar una factura de servicio publico
    4. Crear, eliminar o buscar una cuenta
    0. Salir
    """)
def menu_retirar():
    print("""
    De donde desea retirar?
    1. cuenta de ahorros
    2. tarjeta de credito
    3. cuenta corriente
    4. giro nacional
    5. giro internacional
    0. Volver al menu anterior
            """)
def menu_consignar():
     print("""
    1. Consignar dinero a una cuenta de ahorros
    2. Consignar dinero de una cuenta corriente
    3. Consignar un giro nacional
    4. Consignar un giro internacional
    0. Volver al menu anterior
    """)

def menu_facturas():
    print("""
    Que servicio desea pagar?
    1. Servicio de energía
    2. Servicio de agua
    3. Servicio de gas natural
    0. Volver al menu anterior
    """)

def menu_cuentas():
    print("""
    Que deseas hacer?
    1. Crear una cuenta 
    2. Eliminar una cuenta 
    3. Buscar una cuenta 
    0. Volver al menu anterior
    """)
        
def run():
    if login():
        print(f"Bienvenido al BancoVelandia {user_data['nombre']}, su mejor aliado financiero")
        while True:
            #imprimimos el menu principal
            menu_principal()
            opcion_principal=input("Seleccione una opcion: ")
            #opcion para retirar dinero de varias cuentas
            if opcion_principal=="1":
                #imprimimos el menu de retirar
                menu_retirar()
                opcion_retirar=input("Seleccione una opcion: ") 
                if opcion_retirar=="1":
                    retirar_dinero('saldo_ahorros')
                elif opcion_retirar=="2":
                    retirar_dinero('saldo_tarjeta_credito')
                elif opcion_retirar=="3":
                    retirar_dinero('saldo_corriente')
                elif opcion_retirar=="4":
                    retirar_dinero('saldo_giro_nacional')
                elif opcion_retirar=="5":
                    retirar_dinero('saldo_giro_internacional')
                elif opcion_retirar=="0":
                    break
                else:
                    print("Opcion invalida. Intente nuevamente: ")
            elif opcion_principal == "2":
                #imprimimos el menu de consignar
                menu_consignar()
                opcion=input("Seleccione una opcion: ") 
                if opcion=="1": #consignar cuenta ahorro
                    consignar('cuenta_ahorros','saldo_ahorros')
                elif opcion=="2":
                    consignar('cuenta_corriente','saldo_corriente')
                elif opcion=="3":
                    pass
                elif opcion=="4":
                    pass
                elif opcion=="0":
                    pass
                else:
                    print("Opcion invalida. Intente nuevamente: ")
            elif opcion_principal=="3":  
                
                opcion=input("Seleccione una opcion: ") 
                if opcion=="1":
                    pass
                elif opcion=="2":
                    pass
                elif opcion=="3":
                    pass
                elif opcion=="0":
                    pass
                else:
                    print("Opcion invalida. Intente nuevamente: ")
            elif opcion_principal=="4":  
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
                            saldo=int(input("Debe consignar para que su cuenta sea activada: "))
                            numero_cuenta=random.randint(10**9, 10**10-1) #numero aleatorio de 10 digitos
                elif opcion=="2":
                    pass
                elif opcion=="3":
                    pass
                elif opcion=="0":
                    pass
                else:
                    print("Opcion invalida. Intente nuevamente: ")
            elif opcion_principal=="0":
                print("Gracias por utilizar nuestros servicios.")
                exit()
            else:
                print("Opcion invalida. Intente nuevamente: ")
            #una vez manipulados los dato actualizamos la base de datos
            accounts.actualizar_cuenta(user_data,id_usuario)
    else:
        print('ERROR AL INICIAR SESION')

if __name__ == '__main__':
    run()