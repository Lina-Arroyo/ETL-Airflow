import pandas as pd       
def extract():
    path = "https://raw.githubusercontent.com/Lina-Arroyo/PruebaTecnica/main/Data/Traffic_Flow_Map_Volumes.csv"
    data = pd.read_csv(path)
    return data

def transform(extracted_data = extract()):
    extracted_data.drop_duplicates()
    nulls = extracted_data.isnull().sum()
    if nulls.all() > 1: 
        extracted_data.dropna(axis=1)
    else:
        for col in extracted_data.columns:
            if extracted_data[col].dtype == 'object':
                extracted_data[col] = extracted_data[col].astype('string')
    weather_accidents = extracted_data.groupby('AAWDT')['SEGKEY'].sum() #CONSULTA QUE CALCULA EL NUMERO DE ACCIDENTES POR TIPO DE CLIMA
    return extracted_data

def export(data_transformed = transform()):
    output_file = 'Traffic_Flow_Map_Volumes_TRANSFORMED.csv'
    output_path = f"Data-transformed/{output_file}"
    data_transformed.to_csv(output_path, index=False)
    return data_transformed

print(extract())
print(transform())
print(export())