import time
from random import *


def run_initial_model(params, **kwargs):
    print("--------params: ", params)
    print("kwargs: ", kwargs)
    try:
        file_name = params['file_path']
        fp = open(file_name, 'w+')
        for i in range(20):
            model_value = randint(20, 100)
            print(model_value)
            time.sleep(1)
            fp.write(str(model_value) + '\n')
        fp.close()
    except Exception as e:
        print("Exception|e:", e)

