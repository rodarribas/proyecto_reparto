import pandas as pd


# leer archivos de consumo y devolver número de participantes y consumo total
def analisis_consumos(csvs_consumos):
    numero_archivos = len(csvs_consumos)
    consumo_total = 0
    for csv in csvs_consumos:
        df = pd.read_csv(csv, sep=';')
        df['Consumo'] = df['Consumo'].str.replace(',', '.').astype(float)
        consumo_total += df['Consumo'].sum()
    return f"Número de participantes: {numero_archivos} \n Consumo total: {consumo_total} kWh"
        

# leer archivo de superficies y devolver número de participantes y superficie total
def analisis_superficies(csv_superficies):
    df = pd.read_csv(csv_superficies,
                     header=None,
                     names=['CUPS', 'superficie'])
    participantes = len(df)
    superficie_total = df['superficie'].sum()
    return f"Número de participantes: {participantes} \n Superficie total: {superficie_total} m2"

# leer archivo de superficies y devolver número de participantes y aportación total
def analisis_aportaciones(csv_aportaciones):
    df = pd.read_csv(csv_aportaciones,
                     header=None,
                     names=['CUPS', 'aportacion'])
    participantes = len(df)
    aportacion_total = df['aportacion'].sum()
    return f"Número de participantes: {participantes} \n Aportación total: {aportacion_total} €"

# generar csv
def generar_csv(consumos:list, superficies, aportaciones):
    return None