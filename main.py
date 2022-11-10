import pandas as pd

import math

import numpy as np

import seaborn as sns

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

xlist = []
ylist = []

numforpcc = [
9,
-0.8070007951908298,
-0.8441897849078414,
-0.8573441437602167,
-0.8575546669361195,
-0.8444613893501394,
-0.8135534782018672,
-0.7431567130029479,
-0.623810977258496,
-0.8496662183956072,
-0.9232403150635106,
-0.9059135422262459,
-0.9076481711105561,
-0.9205646736048847,
-0.8643558844276044,
-0.6217720402590438,
-0.09044956872816362,
0.010105108324847222,
0.07369303601621063,
-0.28233969720208646,
-0.44650697763650554,
-0.6634128066843941,
-0.7340331127219839,
-0.7656347873595912,
-0.5856619353311804,
-0.8465512654775593,
-0.8833330112947271,
-0.911937910372616,
-0.9308252097862888,
-0.9563107258452677,
-0.9020946716795573,
-0.6634123104457239,
-0.44697653081377003,
0.13307731872891332,
0.6320931787580414,
0.7620467834971059,
0.7705931034133506,
0.5568993071300697,
0.431858292896024,
0.5460440534428552,
0.5698885134442379,
0.5405809663258248,
0.5065332651776092,
0.5051313542424953,
0.640957548171667,
0.06689568700392558,
-0.31448829773650766,
-0.3683370719879486,
-0.364307644214484,
-0.334686978166886,
-0.06609025577624669,
0.2863719251518567,
0.682505359180391,
0.9360854555075159,
0.9486051820253423,
0.8118550005077103,
0.33381041080731505,
-0.7040711088811247,
-0.6593365330367715,
-0.6160862152614536,
-0.1704695620376885,
-0.022846421286004268,
0.03829453133563268,
-0.234350677086841,
-0.44718742520506327,
-0.41486484394959977,
0.10605346353858551,
0.04561747316047302,
-0.02667083369459658,
-0.22920047171544358,
-0.4965493258474958,
-0.6446165129629615,
-0.3297113342694681,
0.08942831759646182,
0.35954399828672845,
0.2385073479988777,
-0.2900870882980795,
-0.643738980201762,
-0.9300431903425144,
-0.9393303718923061,
-0.8625297711166131,
-0.8127454481681261,
-0.7177635964354625,
-0.4804258929094178,
-0.40425752016384797,
-0.8293129041066543,
-0.9374453894911917,
-0.9688357137835,
-0.9674618984416059,
-0.9766096591850573,
-0.9708305270508965,
-0.7986923774333836,
-0.42050988299674497,
0.3295948957762714,
-0.3664998660875715,
-0.4185473389290413,
-0.39169695948151173,
-0.4610220678091763,
-0.547601386276826,
-0.6175084984939455,
-0.48614834033324655,
-0.18817734804818328,
0.08122821014079137

]
for x in range(1, 103):
    x1 = x + math.log(x, math.exp(1))
    y1 = math.log(numforpcc[x] + 100, math.exp(1))
    xlist.append(x1)
    ylist.append(y1)

print(xlist)
print(ylist)




dd1 = xlist
dd2 = ylist

x = np.array(dd1)
y = np.array(dd2)

a, b = np.polyfit(x, y, 1)
plt.scatter(x, y, color='purple')
plt.plot(x, a*x+b)
plt.plot(x, a*x+b, color='steelblue', linestyle='--', linewidth=2)
plt.text(0, 4.6, 'y = ' + '{:.9f}'.format(b) + ' + {:.9f}'.format(a) + 'x', size=14)
plt.show()
