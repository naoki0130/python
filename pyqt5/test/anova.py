import numpy as np
import scipy as sp
from scipy import stats as st
import pandas as pd

# 正答率
S_E = np.array([48.0, 63.0, 40.0])
S_I = np.array([74.5, 70.6, 43.8])
M_E = np.array([71.6, 73.7, 66.7])
M_I = np.array([84.9, 78.9, 51])
U = np.array([61.3, 61.1, 39.0])

"""
m = np.array([48.0, 61.3, 71.6, 74.5, 84.9])
y = np.array([63.0, 61.1, 73.7, 70.6, 78.9])
a = np.array([40.0, 39.0, 66.7, 43.8, 51])
"""

data = pd.DataFrame({"S_E": S_E, "S_I": S_I, "M_E": M_E, "M_I": M_I, "U": U})
print(data)

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

print()
print()


# 平均解答速度
S_E = np.array([957.5, 933.6])
S_I = np.array([843.9, 795.8])
M_E = np.array([936.1, 899.7])
M_I = np.array([822.8, 924.3])
U = np.array([838, 680.9])

"""
y = np.array([957.5, 838, 936.1, 843.9, 822.8])
a = np.array([933.6, 680.9, 899.7, 795.8, 924.3])
#label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]
"""
"""
S_E = np.array([75.0, 94.4, 57.1])
S_I = np.array([90.5, 100.0, 63.6])
M_E = np.array([88.7, 93.3, 75.0])
M_I = np.array([93.8, 95.7, 72.2])
U = np.array([29.0, 95.7, 51.6])
"""

data = pd.DataFrame({"S_E": S_E, "S_I": S_I, "M_E": M_E, "M_I": M_I, "U": U})
print(data)

print("平均解答速度")
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

print()
print()

# 未解答率
S_E = np.array([36.0, 33.3, 30.0])
S_I = np.array([17.6, 29.4, 31.2])
M_E = np.array([19.3, 21.1, 11.1])
M_I = np.array([9.4, 17.5, 29.4])
U = np.array([29.0, 36.1, 24.4])

"""
m = np.array([36.0, 29.0, 19.3, 17.6, 9.4])
y = np.array([33.3, 36.1, 21.1, 29.4, 17.5])
a = np.array([30.0, 24.4, 11.1, 31.2, 29.4])
#label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]
"""
"""
S_E = np.array([75.0, 94.4, 57.1])
S_I = np.array([90.5, 100.0, 63.6])
M_E = np.array([88.7, 93.3, 75.0])
M_I = np.array([93.8, 95.7, 72.2])
U = np.array([29.0, 95.7, 51.6])
"""

data = pd.DataFrame({"S_E": S_E, "S_I": S_I, "M_E": M_E, "M_I": M_I, "U": U})
print(data)

print("未解答率")
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

print()
print()

# 正答率（未解答を除く）
S_E = np.array([75.0, 94.4, 57.1])
S_I = np.array([90.5, 100.0, 63.6])
M_E = np.array([88.7, 93.3, 75.0])
M_I = np.array([93.8, 95.7, 72.2])
U = np.array([29.0, 95.7, 51.6])

"""
m = np.array([75.0, 29.0, 88.7, 90.5, 93.8])
y = np.array([94.4, 95.7, 93.3, 100.0, 95.7])
a = np.array([57.1, 51.6, 75.0, 63.6, 72.2])
#label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]
"""
"""
S_E = np.array([75.0, 94.4, 57.1])
S_I = np.array([90.5, 100.0, 63.6])
M_E = np.array([88.7, 93.3, 75.0])
M_I = np.array([93.8, 95.7, 72.2])
U = np.array([29.0, 95.7, 51.6])
"""

data = pd.DataFrame({"S_E": S_E, "S_I": S_I, "M_E": M_E, "M_I": M_I, "U": U})
print(data)

print("正答率（未解答を除く）")
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

print()
print()

# 平均思考時間
S_E = np.array([0.338, 0.602, 0.742])
S_I = np.array([0.759, 0.415, 0.732])
M_E = np.array([0.742, 0.487, 0.568])
M_I = np.array([0.631, 0.487, 0.648])
U = np.array([0.471, 1.681, 1.85])

"""
m = np.array([0.338, 0.471, 0.742, 0.759, 0.631])
y = np.array([0.602, 1.681, 0.487, 0.415, 0.487])
a = np.array([0.742, 1.85, 0.568, 0.732, 0.648])
#label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]
"""
"""
S_E = np.array([75.0, 94.4, 57.1])
S_I = np.array([90.5, 100.0, 63.6])
M_E = np.array([88.7, 93.3, 75.0])
M_I = np.array([93.8, 95.7, 72.2])
U = np.array([29.0, 95.7, 51.6])
"""

data = pd.DataFrame({"S_E": S_E, "S_I": S_I, "M_E": M_E, "M_I": M_I, "U": U})
print(data)

print("平均思考時間")
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

print()
print()

# 平均発話時間
S_E = np.array([1.029, 1.054, 1.086])
S_I = np.array([2.495, 2.106, 2.043])
M_E = np.array([1.939, 1.579, 0.75])
M_I = np.array([1.588, 2.186, 1.82])
U = np.array([1.472, 1.471, 1.11])

"""
m = np.array([1.029, 1.472, 1.939, 2.495, 1.588])
y = np.array([1.054, 1.471, 1.579, 2.106, 2.186])
a = np.array([1.086, 1.11, 0.75, 2.043, 1.82])
#label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]
"""
"""
S_E = np.array([75.0, 94.4, 57.1])
S_I = np.array([90.5, 100.0, 63.6])
M_E = np.array([88.7, 93.3, 75.0])
M_I = np.array([93.8, 95.7, 72.2])
U = np.array([29.0, 95.7, 51.6])
"""

data = pd.DataFrame({"S_E": S_E, "S_I": S_I, "M_E": M_E, "M_I": M_I, "U": U})
print(data)

print("平均発話時間")
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
f, p = st.f_oneway(data["S_E"], data["S_I"], data["M_E"], data["M_I"], data["U"])
print("F=%f, p-value = %f" % (f, p))

S_E = data["S_E"]
S_I = data["S_I"]
M_E = data["M_E"]
M_I = data["M_I"]
U = data["U"]


def tukey_hsd(ind, *args):
    # 第1引数:名称のリスト（index）, 第2引数以降: データ (*args: 複数の引数をタプルとして受け取る)

    from statsmodels.stats.multicomp import pairwise_tukeyhsd

    data_arr = np.hstack(args)
    # 配列の結合をhstackでしているらしい．水平方向（新しく列を増やしている方向）に結合．horizontalのhかと

    ind_arr = np.array([])
    for x in range(len(args)):
        ind_arr = np.append(ind_arr, np.repeat(ind[x], len(args[x])))
    # ind_arrの配列の最後にnp.repeat（)を加える
    # np.repeat(A,N)は配列A内の各要素をN回繰り返す

    print(pairwise_tukeyhsd(data_arr, ind_arr))


tukey_hsd(list("S_ES_IM_EM_IU"), S_E, S_I, M_E, M_I, U)
"""
