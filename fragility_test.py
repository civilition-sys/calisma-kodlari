from stochastic_model import g
import numpy as np, statsmodels.api as sm

g2 = g.copy()
g2[500000] += 20

y = g2[1:900000]
X = sm.add_constant(np.column_stack([g2[:-1], np.log(2*np.pi*(np.arange(1,900000)+10))]))
print("Perturbation sonrası ϕ =", sm.OLS(y,X).fit().params[1])