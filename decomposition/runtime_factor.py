import numpy as np
import matplotlib.pyplot as plt

x = np.arange(8, 81, 8)

homoSH=[9.282173157,85.30460787,230.6744361,381.0603254,916.5976729,2383.854894,2955.83834,4134.055677,6772.866756,7330.182154]
awSH=[9.266380072,58.73397589,227.493367,475.9389737,1069.428683,1530.37579,2952.668684,4048.5019,6692.840921,7903.385561]
hetSH=[8.89052844,91.70611191,207.0481138,501.7657037,916.0186565,1568.886369,2924.425771,4099.07664,6735.244641,7484.137447]

homoDH=[39.88793,19.9315302,89.2050569,219.6147438,989.4519612,1706.663503,3792.587216,9292.404918,15921.15787,29466.66694]
awDH=[5.9371698,21.9302091,88.6599189,274.8072741,997.8062594,2193.929447,4655.661571,9560.234359,16360.61499,30411.07332]
hetDH=[5.8046248,24.9652897,90.3998376,314.1849032,999.5404332,2168.174843,4700.970404,9426.238846,15926.37525,29889.25443]

plt.figure(figsize=(10, 6))
plt.plot(x, homoSH, label='homoSH', marker='o')
plt.plot(x, awSH, label='awSH', marker='o')
plt.plot(x, hetSH, label='hetSH', marker='o')
plt.plot(x, homoDH, label='homoDH', marker='o')
plt.plot(x, awDH, label='awDH', marker='o')
plt.plot(x, hetDH, label='hetDH', marker='o')
plt.xlabel('bus size')
plt.ylabel('RunTime')
plt.title('Run time')
plt.xticks(x)
plt.legend()
plt.grid(True)
plt.show()

def estimate_c(xa, xb, xc, ya, yb, yc):
    x = np.concatenate((xa, xb, xc))
    y = np.concatenate((ya, yb, yc))

    # Ensure no division by zero
    valid_indices = x != 0
    ratios = y[valid_indices] / x[valid_indices]

    # Compute the median of ratios
    c_estimate = np.median(ratios)
    return c_estimate

runtime_factor=estimate_c(homoSH,hetSH,awSH,homoDH,hetDH,awDH)

print("runtime_factor:",runtime_factor)