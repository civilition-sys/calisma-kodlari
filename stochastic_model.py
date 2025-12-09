import numpy as np, statsmodels.api as sm
phi, delta, sigma = 0.87143, 12.4290, 1.1190
np.random.seed(42)
g = np.cumsum(np.random.normal(0,sigma,1000000))
g = g - g.mean() + 14.1347251417
for i in range(1,len(g)):
    g[i] = phi*g[i-1] + delta*np.log(2*np.pi*(i+10)) + np.random.normal(0,sigma)

y = g[1:1000000]
X = sm.add_constant(np.column_stack([g[:-1], np.log(2*np.pi*(np.arange(1,1000000)+10))]))
model = sm.OLS(y,X).fit()
print("ϕ =", model.params[1], "R² =", model.rsquared)