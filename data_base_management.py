import pandas as pd
from pandas.core.frame import DataFrame
import re
import numpy as np

df= pd.read_csv("db/db.csv")
df["ID"].fillna("a0", inplace = True)
#df.replace(r'^\s*$', np.nan, regex=True)


contador=0

max_id=df["ID"].max()
n= int(re.sub("\D","",max_id))

for i in range(len(df)):
        n += 1
        contador_format=f"imp{n:04d}"
        df.loc[df['ID'] == 'a0', 'ID'] = contador_format
        # df.loc[i,"ID"] = contador_format

print(df)
# df.set_index("ID",inplace=True)
# df.to_csv("db/db2.csv")