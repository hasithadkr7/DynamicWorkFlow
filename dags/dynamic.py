from airflow import DAG
from airflow.operators.python_operator import PythonOperator,BranchPythonOperator
from datetime import datetime
from model import model_initial, model11, model12, model21, model22, model23, model_final
from condition import branch1, branch2


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 6, 18),
    'email': ['hasitha.10@cse.mrt.ac.lk'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1
}

dag = DAG('check1', default_args=default_args)


model0 = PythonOperator(
    task_id='model0',
    provide_context=True,
    python_callable=model_initial.run_initial_model,
    params={'file_path': '/home/hasitha/airflow/dags/files/input.txt'},
    dag=dag
)

model11 = PythonOperator(
    task_id='model11',
    provide_context=True,
    python_callable=model11.run_model11,
    params={'file_path': '/home/hasitha/airflow/dags/files/input.txt'},
    dag=dag
)

model12 = PythonOperator(
    task_id='model12',
    provide_context=True,
    python_callable=model12.run_model12,
    params={'file_path':'/home/hasitha/airflow/dags/files/input.txt'},
    dag=dag
)

model21 = PythonOperator(
    task_id='model21',
    provide_context=True,
    python_callable=model21.run_model21,
    params={'file_path':'/home/hasitha/airflow/dags/files/model1.txt'},
    dag=dag
)

model22 = PythonOperator(
    task_id='model22',
    provide_context=True,
    python_callable=model22.run_model22,
    params={'file_path':'/home/hasitha/airflow/dags/files/model1.txt'},
    dag=dag
)

model23 = PythonOperator(
    task_id='model23',
    provide_context=True,
    python_callable=model23.run_model23,
    params={'file_path':'/home/hasitha/airflow/dags/files/model1.txt'},
    dag=dag
)

model3 = PythonOperator(
    task_id='model3',
    provide_context=True,
    python_callable=model_final.run_model,
    params={'file_path':'/home/hasitha/airflow/dags/files/output.txt'},
    dag=dag
)

branch1 = BranchPythonOperator(
    task_id='branch1',
    python_callable=branch1.check_branch1_condition,
    dag=dag
)

branch2 = BranchPythonOperator(
    task_id='branch2',
    python_callable=branch2.check_branch2_condition,
    dag=dag
)


model3.set_upstream(model21)
model3.set_upstream(model22)
model3.set_upstream(model23)
model21.set_upstream(branch2)
model22.set_upstream(branch2)
model23.set_upstream(branch2)
branch2.set_upstream(model11)
branch2.set_upstream(model12)
model11.set_upstream(branch1)
model12.set_upstream(branch1)
branch1.set_upstream(model0)