import numpy as np
from scipy import stats as st
import pandas as pd

# 正答率
S_E = np.array([48.0, 63.0, 40.0])
S_I = np.array([74.5, 70.6, 43.8])
M_E = np.array([71.6, 73.7, 66.7])
M_I = np.array([84.9, 78.9, 51])
U = np.array([61.3, 61.1, 39.0])
print(S_E)

data = pd.DataFrame({"S_E": S_E, "S_I": S_I, "M_E": M_E, "M_I": M_I, "U": U})
print(data)

"""
print("正答率")
t, p = st.ttest_ind(data["S_E"], data["M_E"])
# print(data["S_E"], data["M_E"])
print("システム：明示 / 混合：明示　p値 = %(p)s" % locals())
print("--------------------------------------------------------------")

t, p = st.ttest_ind(data["S_I"], data["M_I"])
# print(data["S_I"], data["M_I"])
print("システム：暗黙 / 混合：暗黙　p値 = %(p)s" % locals())
print("--------------------------------------------------------------")
t, p = st.ttest_ind(data["S_E"], data["S_I"])
# print(data["S_E"], data["S_I"])
print("システム：明示 / システム：暗黙　p値 = %(p)s" % locals())
print("--------------------------------------------------------------")
t, p = st.ttest_ind(data["M_E"], data["M_I"])
# print(data["M_E"], data["M_I"])
print("混合：明示 / 混合：暗黙　p値 = %(p)s" % locals())
"""
