import pandas as pd
import numpy as np
import xlrd
import openpyxl

# Zad 1

xlsx = pd.ExcelFile('imiona.xlsx')
odczyt = pd.read_excel(xlsx, header=0)
df = pd.DataFrame(odczyt)
print(df)

# Zad 2

print(df[df['Liczba'] > 1000])

print(df[df['Imie'] == 'MICHAŁ'])

print(df['Liczba'].sum())

df2 = df[((df.Rok >= 2000) & (df.Rok <= 2005))]
print(df2['Liczba'].sum())

ch = df[(df.Plec == 'M')]
dz = df[(df.Plec == 'K')]
print(dz['Liczba'].sum())
print(ch['Liczba'].sum())

