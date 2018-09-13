from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 9, 10),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('prototype_v1', default_args=default_args)

init_wrf0 = BashOperator(
    task_id='init_wrf0',
    bash_command='date',
    dag=dag)

run_wrf0 = BashOperator(
    task_id='run_wrf0',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_wrf0 = BashOperator(
    task_id='upload_wrf0',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_wrf0 = BashOperator(
    task_id='extract_wrf0',
    bash_command='date',
    dag=dag)

init_wrf0 >> run_wrf0 >> upload_wrf0 >> extract_wrf0

init_wrf1 = BashOperator(
    task_id='init_wrf1',
    bash_command='date',
    dag=dag)

run_wrf1 = BashOperator(
    task_id='run_wrf1',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_wrf1 = BashOperator(
    task_id='upload_wrf1',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_wrf1 = BashOperator(
    task_id='extract_wrf1',
    bash_command='date',
    dag=dag)

init_wrf1 >> run_wrf1 >> upload_wrf1 >> extract_wrf1

init_wrf2 = BashOperator(
    task_id='init_wrf2',
    bash_command='date',
    dag=dag)

run_wrf2 = BashOperator(
    task_id='run_wrf2',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_wrf2 = BashOperator(
    task_id='upload_wrf2',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_wrf2 = BashOperator(
    task_id='extract_wrf2',
    bash_command='date',
    dag=dag)

init_wrf2 >> run_wrf2 >> upload_wrf2 >> extract_wrf2

init_hec_single = BashOperator(
    task_id='init_hec_single',
    bash_command='date',
    dag=dag)

run_hec_single = BashOperator(
    task_id='run_hec_single',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_hec_single = BashOperator(
    task_id='upload_hec_single',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_hec_single = BashOperator(
    task_id='extract_hec_single',
    bash_command='date',
    dag=dag)

init_hec_single >> run_hec_single >> upload_hec_single >> extract_hec_single

init_hec_distributed = BashOperator(
    task_id='init_hec_distributed',
    bash_command='date',
    dag=dag)

run_hec_distributed = BashOperator(
    task_id='run_hec_distributed',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_hec_distributed = BashOperator(
    task_id='upload_hec_distributed',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_hec_distributed = BashOperator(
    task_id='extract_hec_distributed',
    bash_command='date',
    dag=dag)

init_hec_distributed >> run_hec_distributed >> upload_hec_distributed >> extract_hec_distributed

init_flo2d_250 = BashOperator(
    task_id='init_flo2d_250',
    bash_command='date',
    dag=dag)

run_flo2d_250 = BashOperator(
    task_id='run_flo2d_250',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_flo2d_250 = BashOperator(
    task_id='upload_flo2d_250',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_flo2d_250 = BashOperator(
    task_id='extract_flo2d_250',
    bash_command='date',
    dag=dag)

init_flo2d_250 >> run_flo2d_250 >> upload_flo2d_250 >> extract_flo2d_250

init_flo2d_150 = BashOperator(
    task_id='init_flo2d_150',
    bash_command='date',
    dag=dag)

run_flo2d_150 = BashOperator(
    task_id='run_flo2d_150',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_flo2d_150 = BashOperator(
    task_id='upload_flo2d_150',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_flo2d_150 = BashOperator(
    task_id='extract_flo2d_150',
    bash_command='date',
    dag=dag)

init_flo2d_150 >> run_flo2d_150 >> upload_flo2d_150 >> extract_flo2d_150

init_flo2d_30 = BashOperator(
    task_id='init_flo2d_30',
    bash_command='date',
    dag=dag)

run_flo2d_30 = BashOperator(
    task_id='run_flo2d_30',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_flo2d_30 = BashOperator(
    task_id='upload_flo2d_30',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_flo2d_30 = BashOperator(
    task_id='extract_flo2d_30',
    bash_command='date',
    dag=dag)

init_flo2d_30 >> run_flo2d_30 >> upload_flo2d_30 >> extract_flo2d_30

init_mike11 = BashOperator(
    task_id='init_mike11',
    bash_command='date',
    dag=dag)

run_mike11 = BashOperator(
    task_id='run_mike11',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

upload_mike11 = BashOperator(
    task_id='upload_mike11',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

extract_mike11 = BashOperator(
    task_id='extract_mike11',
    bash_command='date',
    dag=dag)

init_mike11 >> run_mike11 >> upload_mike11 >> extract_mike11



