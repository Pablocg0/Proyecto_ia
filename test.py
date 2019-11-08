import pandas as pd

diccionario = pd.read_csv("dick_1.csv")
palabra = diccionario["a"].sample(n=10)
palabra.to_csv("dick.csv",encoding='utf-8',index=False)
