from my_package import utils
import pandas as pd

path='my_package/datos.xlsx'
xls = pd.ExcelFile(path)
df_existente = xls.parse('users')

def crear_usuario(nombre,cedula,contraseña):
    #datos que vamos a agregar al excel
    nueva_cuenta={"nombre":[nombre],
                  "cedula":[cedula],
                  "contraseña":[contraseña],
                  "cuenta_ahorros":[''],
                  "saldo_ahorros":[0],
                  "cuenta_corriente":[''],
                  "saldo_corriente":[0],
                  "tarjeta_credito":[''],
                  "saldo_tarjeta_credito":[0],
                  "datacredito":[False],
                  "admin":[False]
                  }
    # Convertir los nuevos datos a un DataFrame
    df_nuevos_datos = pd.DataFrame(nueva_cuenta)
    # Concatenar DataFrames
    df_resultante = pd.concat([df_existente, df_nuevos_datos], ignore_index=True)
    # Escribir de nuevo al archivo Excel
    utils.write_to_excel(df_resultante)
    
def actualizar_cuenta(data,id):
    for columna, valor in data.items():
        df_existente.at[id[0], columna] = valor
    utils.write_to_excel(df_existente,'users')

def crear_cuenta_ahorro(cuenta_ahorros,saldo_ahorros):
    pass

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