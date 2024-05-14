import pandas as pd
import numpy as np
import ADP_NL_cases as cases
import cvxpy as cp
import math
from cvxpy.error import SolverError
import mosek

eps=1e-5

def UP_t(c,a1, a2, a3, b, tau):
    result=1-1/(1+math.exp(a1*tau[0])+sum(math.exp(a2[j]) for j in range(c))**tau[1]
          +sum(math.exp(a3[j]) for j in range(c))**tau[2])
    return result

def UP_1(c,a1, a2, a3, b, tau):
    result=math.exp(tau[0]*(a1))/(math.exp(tau[0]*(a1))+1)
    return result

def UP_2(j, c, a1, a2, a3, b, tau):
    result = math.exp(a2[j]) * sum(math.exp(a2[j]) for j in range(c)) ** (tau[1] - 1) / (
                1 + sum(math.exp(a2[j]) for j in range(c)) ** (tau[1]))
    return result

def UP_3(j, c, a1, a2, a3, b, tau):
    result = math.exp(a3[j]) * sum(math.exp(a3[j]) for j in range(c)) ** (tau[2] - 1) / (
            1 + sum(math.exp(a3[j]) for j in range(c)) ** (tau[2]))
    return result

def E(j,c):
    result=[0 for j in range(c)]
    result[j]=1
    return result

def r1(p1,p2,p3,a1, a2, a3, b, tau):
    if p1<=0:
        result=0
    else:
        result=a1/b[0]+1/b[0]*1/tau[0]*(math.log(1-p1-sum(p2)-sum(p3))-math.log(p1))
    return result

def r2(j,p1,p2,p3,a1, a2, a3, b, tau):
    if p2[j]<=0:
        result=0
    else:
        result=a2[j]/b[1]+1/b[1]*(math.log(1-p1-sum(p2)-sum(p3))-math.log(p2[j]))+1/b[1]*(1-tau[1])/tau[1]*(math.log(1-p1-sum(p2)-sum(p3))-math.log(sum(p2)))
    return result

def r3(j,p1,p2,p3,a1, a2, a3, b, tau):
    if p3[j]<=0:
        result=0
    else:
        result=a3[j]/b[2]+1/b[2]*(math.log(1-p1-sum(p2)-sum(p3))-math.log(p3[j]))+1/b[2]*(1-tau[2])/tau[2]*(math.log(1-p1-sum(p2)-sum(p3))-math.log(sum(p3)))

    return result

def read(c,choice):
    folder_path = "SBD_NL"
    file_name = "DLPnorm" + str(choice) + "capacity" + str(c) + ".txt"
    file_path = f"{folder_path}/{file_name}"
    w = np.loadtxt(file_path)

    folder_path = "SBD_NL/"
    file_name = "SBD_NL_DPtable" + str(choice) + "capacity" + str(c)  + ".txt"
    file_path = f"{folder_path}/{file_name}"
    Vy = np.loadtxt(file_path)

    return Vy,w

def choose_choice(choice,c):
    if choice==0:
        a1, a2, a3, b, tau = cases.homo_seats(c)
    elif choice==1:
        a1, a2, a3, b, tau = cases.incre_seats(c)
    elif choice == 2:
        a1, a2, a3, b, tau = cases.aw_seats(c)
    return a1, a2, a3, b, tau

def Simulation(c,choice):

    T=c*2
    a1, a2, a3, b, tau=choose_choice(choice,c)
    p0 = cp.Variable(1, name="p0")
    p1 = cp.Variable(1, name="p1")
    p2 = cp.Variable(1, name="p2")
    p3 = cp.Variable(1, name="p3")
    p2j = cp.Variable(c, name="p2j")
    p3j = cp.Variable(c, name="p3j")

    x = np.full(c,1)
    y = c

    Revenue=0
    Vy,w=read(c,choice)

    for t in range(T,0,-1):
        if y==0:
            break

        if y==1:
            objective_cp = 1 / (b[0] * tau[0]) * (-cp.kl_div(p1, p0) + p0 - p1) + a1 / b[0] * p1 + p1 * Vy[t - 1, y - 1] \
                           + cp.sum(
                [1 / b[1] * (-cp.kl_div(p2j[j], p0) + p0 - p2j[j]) + a2[j] / b[1] * p2j[j] - (
                            w[j] - Vy[t - 1, y - 1]) *
                 p2j[j] for j in range(c)]) \
                           + 1 / b[1] * (1 - tau[1]) / tau[1] * (-cp.kl_div(p2, p0) - p2 + p0) \
                           +p0*Vy[t-1,y]+ sum(w[j] * x[j] for j in range(c))
        else:
            objective_cp = 1 / (b[0] * tau[0]) * (-cp.kl_div(p1, p0) + p0 - p1) + a1 / b[0] * p1 + p1*Vy[t-1,y-1] \
                           + cp.sum(
                [1 / b[1] * (-cp.kl_div(p2j[j], p0) + p0 - p2j[j]) + a2[j] / b[1] * p2j[j] - (w[j]-Vy[t-1,y-1]) *
                 p2j[j] for j in range(c)]) \
                           + 1 / b[1] * (1 - tau[1]) / tau[1] * (-cp.kl_div(p2, p0) - p2 + p0) \
                           + cp.sum([1 / b[2] * (-cp.kl_div(p3j[j], p0) + p0 - p3j[j]) + a3[j] / b[2] * p3j[j] -(w[j]+w[j - (-1) ** (j + 1)]-Vy[t-1,y-2]) * p3j[j] for j in range(c)]) \
                           + 1 / b[2] * (1 - tau[2]) / tau[2] * (-cp.kl_div(p3, p0) - p3 + p0)+p0*Vy[t-1,y]+sum(w[j]*x[j] for j in range(c))
        objective = cp.Maximize(objective_cp)
        if __name__ == "__main__":
            print('time period t=', t)


        constraints = [p1 <= 1,
                       p1 >= eps,
                       p0 >= eps,
                       p0 <= 1,
                       p2 >= eps,
                       p2 <= 1,
                       p3 >= eps,
                       p3 <= 1,
                       p1 + p0 + p2 + p3 == 1,
                       p2 == cp.sum(p2j),
                       p3 == cp.sum(p3j),
                       p0>= 1-UP_t(c, a1, a2, a3, b, tau)]
        for j in range(c):
            constraints = constraints + [p2j[j] <= x[j]+eps/c,
                                         p3j[j] <= x[j]+eps/c,
                                         p3j[j] <= x[j - (-1) ** (j + 1)]+eps/c,
                                         p1 <= y+eps,
                                         p2j[j] <= y+eps/c,
                                         p3j[j] <= math.floor(y / 2)+eps/c,
                                         p2j[j] <= 1,
                                         p3j[j] <= 1,
                                         p2j[j] >= eps/c,
                                         p3j[j] >= eps/c]
        subp = cp.Problem(objective, constraints)
        try:
            subp.solve(solver=cp.MOSEK)
            if math.isnan(subp.value):
                subp.solve(solver=cp.SCS)
            pass
        except cp.error.SolverError as e:
            subp.solve(solver=cp.SCS)
        if p0[0].value is None or p1[0].value is None or p2[0].value is None or p3[0].value is None:
            subp.solve(solver=cp.SCS)


        if p0[0].value is None or p1[0].value is None or p2[0].value is None or p3[0].value is None:
            raise ValueError("None again, tried=", p0[0].value ,p1[0].value,p2[0].value,p3[0].value)
        p00 = p0[0].value
        p10 = p1[0].value
        p20 = p2[0].value
        p30 = p3[0].value
        p2j0 = p2j.value
        p3j0 = p3j.value
        obj_value = subp.value
        if __name__ == "__main__":
            print("expected revenue at time:",obj_value)

        price1=r1(p10,p2j0,p3j0,a1, a2, a3, b, tau)
        price2=[r2(j,p10,p2j0,p3j0,a1, a2, a3, b, tau) for j in range(c)]
        price3 = [r3(j, p10,p2j0,p3j0,a1, a2, a3, b, tau) for j in range(c)]

        if __name__ == "__main__":
            print(price1)
            print(price2)
            print(price3)
        try:
            buy_product = np.random.choice([0, 1,2,3],
                                    p=[p00,p10,p20,p30])
        except ValueError as e:
            print(e)
            print(p00+p10+p20+p30)
            prob=[p00,p10,p20,p30]/(p00+p10+p20+p30)
            buy_product = np.random.choice([0, 1, 2, 3],
                                           p=prob)
        if buy_product==0:
            if __name__ == "__main__":
                print('no buy')
            continue
        elif buy_product==1:
            if __name__ == "__main__":
                print('buy 1')
                print(price1)
            Revenue=Revenue+price1
            y=y-1
        elif buy_product==2:
            prob=[p2j0[j] / p20 for j in range(c)]
            if sum(prob)!=1:
                round=sum(prob)
                prob=[p2j0[j] / p20/round for j in range(c)]
            buyseats = np.random.choice([j  for j in range(c)],
                                        p=prob)
            if __name__ == "__main__":
                print('buy 2:', buyseats)
                print(price2[buyseats])

            if x[buyseats]==0:
                continue
            else:
                Revenue = Revenue + price2[buyseats]
                y = y - 1
                x[buyseats]=0
        elif buy_product==3:
            prob = [p3j0[j] / p30 for j in range(c)]
            if sum([p3j0[j] / p30 for j in range(c)]) != 1:
                round = sum([p3j0[j] / p30 for j in range(c)])
                prob = [p3j0[j] / p30 / round for j in range(c)]
            buyseats = np.random.choice([j for j in range(c)],
                                        p=prob)
            if __name__ == "__main__":
                print('buy 3:', buyseats)
                print(price3[buyseats])
            y = y - 2
            if x[buyseats]==0 or x[buyseats - (-1) ** (buyseats + 1)] == 0:
                continue
            else:
                Revenue = Revenue + price3[buyseats]
                x[buyseats] = 0
                x[buyseats - (-1) ** (buyseats + 1)] = 0

    if __name__ == "__main__":
        print('ultimate:',Revenue)
    return Revenue

def simu_error_proofed(c,choice):
    try:
        Revenue=Simulation(c,choice)
        return Revenue

    except SolverError as e:
        print(f"SolverError: {e}")
        return "SolverError"


if __name__ == "__main__":
    Revenue=simu_error_proofed(8,0)
    print(Revenue)