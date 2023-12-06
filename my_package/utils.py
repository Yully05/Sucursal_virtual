import pandas as pd

path='my_package/datos.xlsx'
xls = pd.ExcelFile(path)
df_existente = xls.parse('Hoja1')

def write_to_excel(df):
        with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name="Hoja1", index=False)