import pandas as pd

def write_to_excel(df,name,path):
        with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name=name, index=False)

