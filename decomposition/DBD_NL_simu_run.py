import DBD_NL_simu as run
import multiprocessing as multip
import numpy as np
import pandas as pd
import cvxpy as cp
from cvxpy.error import SolverError
import time

'''
0 indicates homo seats
1 indicates incre seats
2 indicates aw seats
'''


def run_Simulator():
    c = 40
    for choice in range(3):
        print('number of processors:', multip.cpu_count())
        print("choice:",choice)
        pool = multip.Pool(multip.cpu_count())
        start_time = time.time()
        results = [pool.apply(run.simu_error_proofed, args=(c, choice)) for t in range(100)]
        pool.close()
        end_time = time.time()

        print(results)
        print('average:', np.mean(results))
        print('variance:', np.var(results))
        print('time:', end_time - start_time)
        folder_path = "../simu_BB"
        file_name = "choice" + str(choice) + "capacity" + str(c) + ".txt"
        file_path = f"{folder_path}/{file_name}"
        np.savetxt(file_path, results)


if __name__ == '__main__':
    run_Simulator()