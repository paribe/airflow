from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Definição da DAG
with DAG(
    dag_id="bash_operator_test_dag",      # Nome único da DAG
    start_date=datetime(2023, 12, 1),    # Data de início para execução
    schedule_interval=None,              # Sem agendamento (executa manualmente)
    catchup=False,                       # Ignora execuções anteriores
    tags=["teste"],                      # Tags para organização no Airflow UI
) as dag:

    # Tarefa 1: Criar um arquivo de texto
    create_file = BashOperator(
        task_id="create_file",             # Nome único da tarefa
        bash_command="echo 'Airflow Test - Hello World' > /tmp/airflow_test.txt"  # Comando shell
    )

    # Tarefa 2: Ler o conteúdo do arquivo
    read_file = BashOperator(
        task_id="read_file",               # Nome único da tarefa
        bash_command="cat /tmp/airflow_test.txt"  # Comando shell
    )

    # Definindo a sequência de execução
    create_file >> read_file  # A tarefa read_file só será executada após create_file
