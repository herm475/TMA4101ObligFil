import numpy as np
import matplotlib.pyplot as plt

def v(t):
    return 10* (1 - np.e**(-t/100))
def v_min(t):
    return 10* (1 - np.e**(-t/101))
def v_max(t):
    return 10* (1 - np.e**(-t/99))

t_verdier = np.linspace(0, 735, 2000)

reelT = [0,11.78,24.9,42,61,84,115,137,163,201,266,456,735]
reelV = [0.036,1,2,3,4,5,6,6.5,7,7.5,8,8.5,8.62]

plt.plot(t_verdier, v(t_verdier), label='v(t)')
plt.plot(t_verdier, v_min(t_verdier), label='v_min')
plt.plot(t_verdier, v_max(t_verdier), label='v_max')
plt.plot(reelT, reelV, 'o', label='Målte verdier for kretsen i praksis')
for i, txt in enumerate(reelV):
    plt.text(reelT[i], reelV[i], f'{txt:.2f}V', fontsize=9, ha='right')
plt.grid()
plt.xlabel('t: sekunder')
plt.ylabel('v(t): Spenning over kondensator')
plt.legend()
plt.savefig('RC-krets.png')
