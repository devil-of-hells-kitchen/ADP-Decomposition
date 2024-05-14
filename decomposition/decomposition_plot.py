import matplotlib.pyplot as plt
import numpy as np
x=[8,16,24,32,40,48,56,64,72,80]

def regular(a):
    a = [a[i] / (i + 1) / 8 for i in range(len(a))]
    return a
def fill(a):
    n=len(x)-len(a)
    if n <0:
        raise Exception("x too short")
    a=np.append(a,np.full(n,np.nan))
    return a

def check(a):
    a=regular(a)
    a=fill(a)
    return a

width=2
marksize=10
plt.rcParams['font.size'] = 14
#homo
SBD_UB=np.array([68.19310778,156.886865,253.8413461,356.2919813,462.8982624,572.8590697,685.6397759,800.8566531,918.2200106,1037.503977])#done,10 #done
DBD_UB=fill(np.array([68.20755474,157.4561226,253.9768079,356.6548509,467.6632643]))
SBDb_UB=np.array([68.19310778,156.886865,253.8413461,356.2919813,462.8982624,572.8590697,685.6397759,800.8566531,918.2200106,1037.503977])#done,10 #done
DBDb_UB=fill(np.array([68.20755474,157.4561226,253.9768079]))
aALP=fill(np.array([72.8403, 163.8807,261.7514,365.4608,472.9219,583.7837]))#done,7
DLPflex=fill(np.array([73.4672,164.2791, 262.6809, 366.2465, 473.7669,584.5070,697.9593,813.7966,931.7119,1051.4982]))#done,10 #done
SBD_simu=fill(np.array([65.18090367,146.4762095,233.8683899,322.0946331,415.5601903,516.7127726,617.6334809,717.5733745,806.4080793,928.1086631]))#done,10 #done
SBD_ke_simu=fill(np.array([63.40814352,144.8585631,229.8516274,325.2756883,421.9690381,517.9774304,616.2465004,720.332819,821.1760017,939.4756403]))#done,10 #done
DBD_simu=fill(np.array([64.0650882,145.8404489,229.9263386,322.3793577,417.214446]))
DBD_ke_simu=fill(np.array([63.50914597,139.6083428,227.2742662]))
aALP_simu=fill(np.array([61.51645966, 140.4090248,228.0410353, 327.8085561, 405.9912876, 515.2261522]))
sbADP_simu=fill(np.array([65.6175, 147.1951, 235.3542, 325.4653, 417.7427,520.5485, 623.3708,719.012,803.6387,931.8864]))#done,10 #done
DLP_simu=fill(np.array([61.76868903,136.6434638,225.8983885,321.653457,408.8678216,521.1925854,606.4922439,704.231146,817.0857212,915.4330941])) #done
#upper bounds
plt.figure(figsize=(10, 6))

plt.plot(x, SBD_UB/SBD_UB, label='UB SDPD',color='forestgreen', marker='o',markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DBD_UB/SBD_UB, label='UB DPD',color='lightsteelblue', marker='s', markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, SBDb_UB/SBD_UB, label='UB SDPD-Benchmark',color='orange', marker='x',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, DBDb_UB/SBD_UB, label='UB DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, aALP/SBD_UB, label='UB AFF',color='black', marker='^', linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DLPflex/SBD_UB, label='UB DPP',color='violet', marker='.', linestyle='-', linewidth=width, markersize=10)


plt.xticks(x)
plt.xlabel('Bus Size')
plt.ylabel('Expected Revenue Upper Bound')
#plt.title('Expected Revenue Upper Bound for Homogeneous Seats')
plt.legend()

#pricing policies
plt.figure(figsize=(10, 6))

plt.plot(x, SBD_simu/SBD_UB, label='Policy SDPD',color='forestgreen', marker='o',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, DBD_simu/SBD_UB, label='Policy DPD',color='lightsteelblue', marker='s',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, SBD_ke_simu/SBD_UB, label='Policy SDPD-Benchmark',color='orange', marker='x', markerfacecolor='none',linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, DBD_ke_simu/SBD_UB, label='Policy DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, aALP_simu/SBD_UB, label='Policy AFF',color='black', marker='^', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x,DLP_simu/SBD_UB,label='Policy DPP',color='violet', marker='.', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, sbADP_simu/SBD_UB, label='Policy sbADP (M=100)',color='salmon', marker='<', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, SBD_UB/SBD_UB, label='UB SDPD',color='forestgreen', marker='o',markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DBD_UB/SBD_UB, label='UB DPD',color='lightsteelblue', marker='s', markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, SBDb_UB/SBD_UB, label='UB SDPD-Benchmark',color='orange', marker='x',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, DBDb_UB/SBD_UB, label='UB DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, aALP/SBD_UB, label='UB AFF',color='black', marker='^', linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DLPflex/SBD_UB, label='UB DPP',color='violet', marker='.', linestyle='-', linewidth=width, markersize=10)

plt.xticks(x)
plt.ylim(0.85, 1.2)
plt.xlabel('Bus Size',fontsize=14)
plt.ylabel('Revenue',fontsize=14)
#plt.title('Pricing Policies for Homogeneous Seats')
plt.legend(ncol=2)

#aw2
SBD_UB=fill(np.array([68.68107321,158.0035498,255.6408439,358.8093908,466.159216,576.8840245,690.4451588,806.4563508,924.6261723,1044.727118]))#done,10
DBD_UB=fill(np.array([68.85054879,158.8803758,255.7254855,358.9721947,466.3530573]))
SBDb_UB=fill(np.array([68.68107321,158.0035498,255.6408439,358.8093908,466.159216,576.8840245,690.4451588,806.4563508,924.6261723,1044.727118]))#done,10
DBDb_UB=fill(np.array([68.85054879,158.8803758,255.7254855]))
aALP=fill(np.array([73.5945, 165.3088, 263.5421,367.8312, 476.1498,587.6852765]))
DLPflex=fill(np.array([73.9693, 165.4193, 264.5128, 368.8046, 477.0683,588.5881, 702.8386, 819.4657,938.1937,1058.8027]))#done,10
SBD_simu=fill(np.array([65.95247985,147.3883303,234.8434855,324.4136242,417.742841,519.8542781,622.1916855,721.9051365,828.3652528,933.3906669]))#done,10
SBD_ke_simu=fill(np.array([64.80389228,142.4825172,229.1730246,331.2937696,424.3623961,524.8135163,614.9857374,719.5939388,825.3152476,935.7446573]))#done,10
DBD_simu=fill(np.array([61.70406798,146.9522938,234.3609019,326.3842427,420.499351]))
DBD_ke_simu=fill(np.array([65.12146265,147.7710175,233.0666979]))
aALP_simu=fill(np.array([64.2027,141.4453,232.2628,318.2689,420.7110095,533.7769]))
sbADP_simu=fill(np.array([66.5168, 148.5609, 237.0439, 327.5639, 421.196,525.2066, 624.6149,723.7956,832.6958]))
DLP_simu=fill(np.array([62.73921092,142.4533388,227.9844272,319.7337776,413.6970296,514.2426029,623.8092616,712.3248581,825.3080272,932.1231979]))

#upper bounds
plt.figure(figsize=(10, 6))

plt.plot(x, SBD_UB/SBD_UB, label='UB SDPD',color='forestgreen', marker='o',markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DBD_UB/SBD_UB, label='UB DPD',color='lightsteelblue', marker='s', markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, SBDb_UB/SBD_UB, label='UB SDPD-Benchmark',color='orange', marker='x',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, DBDb_UB/SBD_UB, label='UB DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, aALP/SBD_UB, label='UB AFF',color='black', marker='^', linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DLPflex/SBD_UB, label='UB DPP',color='violet', marker='.', linestyle='-', linewidth=width, markersize=10)

plt.xticks(x)
plt.xlabel('Bus Size',fontsize=14)
plt.ylabel('Expected Revenue Upper Bound',fontsize=14)
#plt.title('Expected Revenue Upper Bound for Window Aisle Seats')
plt.legend()

plt.figure(figsize=(10, 6))

plt.plot(x, SBD_simu/SBD_UB, label='Policy SDPD',color='forestgreen', marker='o',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, DBD_simu/SBD_UB, label='Policy DPD',color='lightsteelblue', marker='s',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, SBD_ke_simu/SBD_UB, label='Policy SDPD-Benchmark',color='orange', marker='x', markerfacecolor='none',linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, DBD_ke_simu/SBD_UB, label='Policy DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, aALP_simu/SBD_UB, label='Policy AFF',color='black', marker='^', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x,DLP_simu/SBD_UB,label='Policy DPP',color='violet', marker='.', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, sbADP_simu/SBD_UB, label='Policy sbADP (M=500)',color='salmon', marker='<', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, SBD_UB/SBD_UB, label='UB SDPD',color='forestgreen', marker='o',markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DBD_UB/SBD_UB, label='UB DPD',color='lightsteelblue', marker='s', markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, SBDb_UB/SBD_UB, label='UB SDPD-Benchmark',color='orange', marker='x',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, DBDb_UB/SBD_UB, label='UB DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, aALP/SBD_UB, label='UB AFF',color='black', marker='^', linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DLPflex/SBD_UB, label='UB DPP',color='violet', marker='.', linestyle='-', linewidth=width, markersize=10)

plt.xticks(x)
plt.ylim(0.85, 1.2)
plt.xlabel('Bus Size',fontsize=14)
plt.ylabel('Revenue',fontsize=14)
#plt.title('Pricing Policies for Window Aisle Seats')
plt.legend(ncol=2)

#hete1
SBD_UB=fill(np.array([68.5763,158.7802,258.5238,365.1316,477.3276,594.3414,715.6614,840.9240878,969.864613,1102.264783]))
DBD_UB=fill(np.array([68.73937214,159.3815067,258.4787941,365.0597056]))
SBDb_UB=fill(np.array([68.5763,158.7802,258.5238,365.1316,477.3276,594.3414,715.6614,840.9240878,969.864613,1102.264783]))
DBDb_UB=fill(np.array([68.73937214,159.3815067,258.4787941]))
aALP=fill(np.array([73.2709,165.9500,266.4274,374.1611,487.1153]))
DLPflex=fill(np.array([73.8903,166.2737,267.5327,375.3259,488.4989,606.3513,728.4132,854.347,983.8986,1116.869]))
SBD_simu=fill(np.array([65.7301,147.9944,237.5788,329.5121,428.3583,534.316 ,642.0496,751.0935224,868.1036434,983.2366525]))
SBD_ke_simu=fill(np.array([66.30000208,148.419747,237.3460033,340.4268253,429.4230131,532.0028433,643.2665254,754.3857147,863.9829838,991.4897978]))
DBD_simu=fill(np.array([65.56442948,143.9237597,230.9097866,333.1806937]))
DBD_ke_simu=fill(np.array([63.50814169,145.1733577,230.4385026]))
aALP_simu=fill(np.array([63.1212,139.4511,228.9911,315.6564,430.6832563]))
sbADP_simu=fill(np.array([0.4257,148.6668,239.3339,332.8899,430.6909,538.6876,646.57,389.9259,870.4187]))
DLP_simu=fill(np.array([62.81937392,140.4548377,233.0183761,327.9570462,428.9232835,528.5246355,642.5287456,753.3805795,855.5800148,979.7573685]))
#upper bounds
plt.figure(figsize=(10, 6))

plt.plot(x, SBD_UB/SBD_UB, label='UB SDPD',color='forestgreen', marker='o',markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DBD_UB/SBD_UB, label='UB DPD',color='lightsteelblue', marker='s', markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, SBDb_UB/SBD_UB, label='UB SDPD-Benchmark',color='orange', marker='x',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, DBDb_UB/SBD_UB, label='UB DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, aALP/SBD_UB, label='UB AFF',color='black', marker='^', linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DLPflex/SBD_UB, label='UB DPP',color='violet', marker='.', linestyle='-', linewidth=width, markersize=10)

plt.xticks(x)
plt.xlabel('Bus Size',fontsize=14)
plt.ylabel('Expected Revenue Upper Bound',fontsize=14)
#plt.title('Expected Revenue Upper Bound for Heterogeneous Seats')
plt.legend()

plt.figure(figsize=(10, 6))

plt.plot(x, SBD_simu/SBD_UB, label='Policy SDPD',color='forestgreen', marker='o',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, DBD_simu/SBD_UB, label='Policy DPD',color='lightsteelblue', marker='s',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, SBD_ke_simu/SBD_UB, label='Policy SDPD-Benchmark',color='orange', marker='x', markerfacecolor='none',linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, DBD_ke_simu/SBD_UB, label='Policy DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, aALP_simu/SBD_UB, label='Policy AFF',color='black', marker='^', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x,DLP_simu/SBD_UB,label='Policy DPP',color='violet', marker='.', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, sbADP_simu/SBD_UB, label='Policy sbADP (M=500)',color='salmon', marker='<', linestyle=':', linewidth=width, markersize=marksize)
plt.plot(x, SBD_UB/SBD_UB, label='UB SDPD',color='forestgreen', marker='o',markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DBD_UB/SBD_UB, label='UB DPD',color='lightsteelblue', marker='s', markerfacecolor='none',linestyle='-', linewidth=width, markersize=10)
plt.plot(x, SBDb_UB/SBD_UB, label='UB SDPD-Benchmark',color='orange', marker='x',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, DBDb_UB/SBD_UB, label='UB DPD-Benchmark',color='crimson', marker='+',markerfacecolor='none', linestyle='--', linewidth=width, markersize=10)
plt.plot(x, aALP/SBD_UB, label='UB AFF',color='black', marker='^', linestyle='-', linewidth=width, markersize=10)
plt.plot(x, DLPflex/SBD_UB, label='UB DPP',color='violet', marker='.', linestyle='-', linewidth=width, markersize=10)

plt.xticks(x)
plt.ylim(0.85, 1.2)
plt.xlabel('Bus Size',fontsize=14)
plt.ylabel('Revenue',fontsize=14)
#plt.title('Pricing Policies for Heterogeneous Seats')
plt.legend(ncol=2)

plt.show()