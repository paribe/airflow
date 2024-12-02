from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Função Python simples
def hello_airflow():
    print("Hello, Airflow! Este é um teste básico da sua instalação.")

# Configuração da DAG
with DAG(
    dag_id="example_hello_airflow",  # Nome da DAG
    default_args={
        "owner": "airflow",
        "retries": 1,
    },
    description="DAG de exemplo para testar o Airflow",
    schedule_interval=None,  # Não é agendada automaticamente
    start_date=datetime(2023, 1, 1),  # Data de início
    catchup=False,  # Evita executar runs atrasados
) as dag:

    # Tarefa da DAG
    hello_task = PythonOperator(
        task_id="hello_task",  # Nome da tarefa
        python_callable=hello_airflow,  # Função a ser executada
    )

    hello_task  # Define a tarefa na DAG
