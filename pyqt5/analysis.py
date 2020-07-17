import pandas as pd
from scipy import signal, stats
import os
import codecs

# csvfileのパス入力
# print("Please write the directory path:")
# path = input()
csv_file = [i for i in os.listdir(path="output") if i[-3:] == "csv"]

# 選択したいcsvfileの番号入力
print("Please choose csvfile number:")

for i, name in enumerate(csv_file):
    print(i, name)

choose_csv = int(input())


def file_open(data):
    with codecs.open("output/" + data, "r", "Shift-JIS", "ignore") as file:
        df = pd.read_csv(file)
        df = pd.DataFrame(df)
        return df


def file_len(data):
    with codecs.open("output/" + data, "r", "Shift-JIS", "ignore") as file:
        df = pd.read_csv(file)
        return df


df = file_open(csv_file[choose_csv])
df = df.T

l = file_len(csv_file[choose_csv])
print(l)

# Data = pd.DataFrame(df, index=id)
# print(Data)
