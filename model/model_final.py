import time


def run_model(params, **kwargs):
    print("kwargs : ", kwargs)
    try:
        print("params : ", params)
        file_name = params['file_path']
        fp = open(file_name, 'w')
        time.sleep(10)
        fp.write('Work-flow completed..!' + '\n')
        time.sleep(1)
        fp.close()
    except Exception as e:
        print("Exception|e:", e)

