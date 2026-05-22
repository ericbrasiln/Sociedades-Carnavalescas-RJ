import pandas as pd

df = pd.read_csv('/home/ebn/Documentos/GitHub/Sociedades-Carnavalescas-RJ/S_C.csv')

df = df.drop(columns=['IMG', 'Transcrever'])

df.to_csv('S_C2.csv', index=False)
