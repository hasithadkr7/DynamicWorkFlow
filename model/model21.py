import time


def run_model21(params, **kwargs):
    print(kwargs)
    try:
        print("params : ", params)
        input_file = params['file_path']
        print("run_model11|input_file:", input_file)
        #input_file = "/home/hasitha/airflow/dags/worker/model1.txt"
        output_file = "/home/hasitha/airflow/dags/files/model2.txt"
        out_fb = open(output_file, 'a')
        with open(input_file) as fp:
            for line in fp:
                model_value = int(line.strip()) / 5
                print(model_value)
                time.sleep(1)
                out_fb.write(str(model_value)+'\n')
            fp.close()
            out_fb.close()
    except Exception as e:
        print("run_model21|Exception|e:", e)

