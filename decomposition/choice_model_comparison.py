import ADP_NL_cases as cases
import math
import matplotlib.pyplot as plt

choice=0

def choose_choice(choice,c):
    if choice==0:
        a1, a2, a3, b, tau = cases.homo_seats(c)
    elif choice==1:
        a1, a2, a3, b, tau = cases.incre_seats(c)
    elif choice == 2:
        a1, a2, a3, b, tau = cases.aw_seats(c)
    return a1, a2, a3, b, tau

def prob(r1, r2, r3):

    a1, a2, a3, b, tau=choose_choice(choice,c)
    Deno=1+math.exp(a1-r1*b[0])**tau[0]+sum([math.exp(a2[j]-r2[j]*b[1]) for j in range(c)])**tau[1]+sum([math.exp(a3[j]-r3[j]*b[2]) for j in range(c)])**tau[2]
    p1=math.exp(a1-r1*b[0])**tau[0]/Deno
    p=sum([math.exp(a2[j]-r2[j]*b[1]) for j in range(c)])**tau[1]/Deno
    p2=[math.exp(a2[i]-r2[i]*b[1])/sum([math.exp(a2[j]-r2[j]*b[1]) for j in range(c)])*p for i in range(c)]
    p = sum([math.exp(a3[j] - r3[j] * b[2]) for j in range(c)]) ** tau[2] / Deno
    p3 = [math.exp(a3[i] - r3[i] * b[2]) / sum([math.exp(a3[j] - r3[j] * b[2]) for j in range(c)])*p for i in range(c)]

    return p1, p2, p3

choice=0

pro0=[0]*8
pro1=[0]*8
pro2=[0]*8
pro3=[0]*8

for i in range(1,9):
    c=8*i
    r1 = 8
    r2 = [10] * c
    r3 = [14] * c
    p1,p2,p3=prob(r1, r2, r3)
    p0=1-p1-sum(p2)-sum(p3)
    pro0[i - 1] = p0
    pro1[i-1]=p1
    pro2[i - 1] = p2[0]
    pro3[i - 1] = p3[0]
    print(p0,p1,p2[0],p3[0])

x=[8,16,24,32,40,48,56,64]


plt.figure(figsize=(10, 6))

#plt.plot(x, pro0, label='p0')
plt.plot(x, [pro1[i]*8 for i in range(8)], label='p1')
plt.plot(x, [pro2[i]*x[i]*10 for i in range(8)], label='p2')
plt.plot(x, [pro3[i]*x[i]*7 for i in range(8)], label='p3')

plt.xlabel('Bus Size')
plt.ylabel('Expected return per seat')
plt.title('Expected return for Homogeneous Seats with price'+str(r1)+'-'+str(r2[0])+'-'+str(r3[0]))
plt.legend()
plt.xticks(x)

plt.show()