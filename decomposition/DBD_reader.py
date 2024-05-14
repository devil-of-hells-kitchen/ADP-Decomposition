import cvxpy as cp
import numpy as np
import Branch_Bound as BB
import ADP_NL_cases as cases
import math
import time

choice=0
c=16
T=c*2

folder_path = "../BB"
file_name = "part_3_v_value_ADP_NL_CVXPY_choice" + str(choice) + "capacity" + str(c) + "BB_ex.txt"
file_path = f"{folder_path}/{file_name}"
v = np.loadtxt(file_path)
file_name = "part_3_w_value_ADP_NL_CVXPY_choice" + str(choice) + "capacity" + str(c) + "BB_ex.txt"
file_path = f"{folder_path}/{file_name}"
w = np.loadtxt(file_path)
file_name = "part_3_theta_value_ADP_NL_CVXPY_choice" + str(choice) + "capacity" + str(c) + "BB_ex.txt"
file_path = f"{folder_path}/{file_name}"
theta = np.loadtxt(file_path)

folder_path = "DBD_NL"
file_name = "DBD_NL_DPtable" + str(choice) + "capacity" + str(c) + ".txt"
file_path = f"{folder_path}/{file_name}"
V = np.loadtxt(file_path)
