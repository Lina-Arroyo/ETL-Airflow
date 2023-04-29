import pandas as pd
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor

default_args = {
    'owner': 'Lina Arroyo',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 27),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract():
    path = "https://raw.githubusercontent.com/Lina-Arroyo/PruebaTecnica/main/Data/Traffic_Flow_Map_Volumes.csv"
    data = pd.read_csv(path)
    json_data = data.to_json()
    return json_data

with DAG('Extract', default_args=default_args, schedule_interval='0 0 * * *') as dagA:
    extraction = PythonOperator(
        task_id='extract',
        python_callable=extract,
        dag=dagA
    )

    extraction

def transform():
    extracted_data = extract()
    extracted_data = pd.read_json(extracted_data)
    extracted_data.drop_duplicates(inplace=True)
    nulls = extracted_data.isnull().sum()
    if nulls.all() > 1: 
        extracted_data.dropna(axis=1, inplace=True)
    else:
        for col in extracted_data.columns:
            if extracted_data[col].dtype == 'object':
                extracted_data[col] = extracted_data[col].astype('string')
    weather_accidents = extracted_data.groupby('AAWDT')['SEGKEY'].sum() #CONSULTA QUE CALCULA EL NUMERO DE ACCIDENTES POR TIPO DE CLIMA
    return extracted_data.to_json()

with DAG('Transform', default_args=default_args, schedule_interval='0 0 * * *') as dagB:
    wait_for_extraction = ExternalTaskSensor(
        task_id='wait_for_extraction',
        external_dag_id='Extract',
        external_task_id='extract',
        dag=dagB
    )

    transformation = PythonOperator(
        task_id='transform',
        python_callable=transform,
        dag=dagB,
        trigger_rule ='all_done'
    )

    wait_for_extraction >> transformation


def export():
    data_transformed = transform()
    data_transformed = pd.read_json(data_transformed)
    output_file = 'Traffic_Flow_Map_Volumes_TRANSFORMED.csv'
    data_transformed.to_csv(output_file, index=False)
    return data_transformed.to_json()

with DAG('Export', default_args=default_args, schedule_interval='0 0 * * *') as dagC:
    wait_for_transformation = ExternalTaskSensor(
        task_id='wait_for_transformation',
        external_dag_id='Transform',
        external_task_id='transform',
        dag=dagC
    )

    exportation = PythonOperator(
        task_id='export',
        python_callable=export,
        dag=dagC,
        trigger_rule='all_done'
    )

    wait_for_transformation >> exportation

'''
ESTE DAG ES UN DAG PARA INTENTAR CARGAR EL CSV YA TRANSFORMADO A UNA CARPETA DENTRO DEL REPOSITORIO.
def save_dataframe_to_csv():
    # Load dataframe from source
    df = pd.read_csv("https://raw.githubusercontent.com/Lina-Arroyo/PruebaTecnica/main/Data/Traffic_Flow_Map_Volumes.csv")

    # Save dataframe as CSV to local folder
    df.to_csv('Traffic_Flow_Map_Volumes_TRANSFORMED.csv', index=False)

with DAG('save_dataframe', default_args=default_args, schedule_interval='0 0 * * *') as dag:
    save_dataframe_to_csv_operator = PythonOperator(
        task_id='save_dataframe_to_csv',
        python_callable=save_dataframe_to_csv,
        dag=dag
    )

    add_to_github_operator = BashOperator(
        task_id='add_to_github',
        bash_command='cd PruebaTecnica/Data-transformed/ && git add Traffic_Flow_Map_Volumes_TRANSFORMED.csv && git commit -m "Data transformada subida con exito" && git push',
        dag=dag
    )

save_dataframe_to_csv_operator >> add_to_github_operator
'''

