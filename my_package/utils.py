import pandas as pd

path='my_package/datos.xlsx'
xls = pd.ExcelFile(path)
df_existente = xls.parse('users')

def write_to_excel(df,name):
        with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name=name, index=False)

