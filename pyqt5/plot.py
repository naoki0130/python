import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = [
    "Hiragino Maru Gothic Pro",
    "Yu Gothic",
    "Meirio",
    "Takao",
    "IPAexGothic",
    "IPAPGothic",
    "VL PGothic",
    "Noto Sans CJK JP",
]

# 正答率
left1 = np.array([1, 2, 3, 4, 5])
left2 = np.array([1.3, 2.3, 3.3, 4.3, 5.3])
left3 = np.array([1.6, 2.6, 3.6, 4.6, 5.6])
m = np.array([48.0, 61.3, 71.6, 74.5, 84.9])
y = np.array([63.0, 61.1, 73.7, 70.6, 78.9])
a = np.array([40.0, 39.0, 66.7, 43.8, 51])
label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]

plt.bar(
    left1,
    m,
    color="r",
    label="M",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left2,
    y,
    color="b",
    label="Y",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left3,
    a,
    color="g",
    label="A",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.title("ゲーム正答率")
plt.xlabel("対話形式")
plt.ylabel("正答率(%)")
plt.grid(zorder=1)

plt.show()

# 未解答率
left1 = np.array([1, 2, 3, 4, 5])
left2 = np.array([1.3, 2.3, 3.3, 4.3, 5.3])
left3 = np.array([1.6, 2.6, 3.6, 4.6, 5.6])
m = np.array([36.0, 29.0, 19.3, 17.6, 9.4])
y = np.array([33.3, 36.1, 21.1, 29.4, 17.5])
a = np.array([30.0, 24.4, 11.1, 31.2, 29.4])
label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]

plt.bar(
    left1,
    m,
    color="r",
    label="M",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left2,
    y,
    color="b",
    label="Y",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left3,
    a,
    color="g",
    label="A",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.title("ゲーム未解答率")
plt.xlabel("対話形式")
plt.ylabel("未解答率(%)")
plt.grid(zorder=1)

plt.show()

# 未解答を除く正答率
left1 = np.array([1, 2, 3, 4, 5])
left2 = np.array([1.3, 2.3, 3.3, 4.3, 5.3])
left3 = np.array([1.6, 2.6, 3.6, 4.6, 5.6])
m = np.array([75.0, 29.0, 88.7, 90.5, 93.8])
y = np.array([94.4, 95.7, 93.3, 100.0, 95.7])
a = np.array([57.1, 51.6, 75.0, 63.6, 72.2])
label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]

plt.bar(
    left1,
    m,
    color="r",
    label="M",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left2,
    y,
    color="b",
    label="Y",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left3,
    a,
    color="g",
    label="A",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.title("ゲーム正答率（未解答を除く）")
plt.xlabel("対話形式")
plt.ylabel("正答率(%)")
plt.grid(zorder=1)

plt.show()

# 平均解答時間
left1 = np.array([1, 2, 3, 4, 5])
left2 = np.array([1.3, 2.3, 3.3, 4.3, 5.3])

y = np.array([957.5, 838, 936.1, 843.9, 822.8])
a = np.array([933.6, 680.9, 899.7, 795.8, 924.3])
label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]

plt.bar(
    left1,
    y,
    color="b",
    label="Y",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left2,
    a,
    color="g",
    label="A",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.title("ゲーム平均解答時間")
plt.xlabel("対話形式")
plt.ylabel("ミリ秒(ms)")
plt.grid(zorder=1)

plt.show()


# 思考時間平均
left1 = np.array([1, 2, 3, 4, 5])
left2 = np.array([1.3, 2.3, 3.3, 4.3, 5.3])
left3 = np.array([1.6, 2.6, 3.6, 4.6, 5.6])
m = np.array([0.338, 0.471, 0.742, 0.759, 0.631])
y = np.array([0.602, 1.681, 0.487, 0.415, 0.487])
a = np.array([0.742, 1.85, 0.568, 0.732, 0.648])
label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]

plt.bar(
    left1,
    m,
    color="r",
    label="M",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left2,
    y,
    color="b",
    label="Y",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left3,
    a,
    color="g",
    label="A",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.title("平均対話思考時間")
plt.xlabel("対話形式")
plt.ylabel("ミリ秒(ms)")
plt.grid(zorder=1)

plt.show()

# 解答時間平均
left1 = np.array([1, 2, 3, 4, 5])
left2 = np.array([1.3, 2.3, 3.3, 4.3, 5.3])
left3 = np.array([1.6, 2.6, 3.6, 4.6, 5.6])
m = np.array([1.029, 1.472, 1.939, 2.495, 1.588])
y = np.array([1.054, 1.471, 1.579, 2.106, 2.186])
a = np.array([1.086, 1.11, 0.75, 2.043, 1.82])
label = ["システム：明示", "ユーザ", "混合：明示", "システム：暗黙", "混合：暗黙"]

plt.bar(
    left1,
    m,
    color="r",
    label="M",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left2,
    y,
    color="b",
    label="Y",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)
plt.bar(
    left3,
    a,
    color="g",
    label="A",
    tick_label=label,
    align="center",
    width=0.3,
    zorder=2,
)

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.title("平均対話発話時間")
plt.xlabel("対話形式")
plt.ylabel("ミリ秒(ms)")

plt.grid(zorder=1)

plt.show()

