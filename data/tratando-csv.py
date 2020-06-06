import pandas as pd
import csv

df = pd.read_csv('/home/ebn/Documentos/GitHub/Sociedades-Carnavalescas-RJ/data/Sociedades Carnavalescas.csv')

df.to_csv('SC-v2.csv', index=True)
