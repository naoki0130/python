import pandas as pd
from scipy import signal, stats
import os
import codecs
import csv
import calc

# csv_file_open
def file_open_correct(data):
    with codecs.open("correct/" + data, "r", "Shift-JIS", "ignore") as file:
        r = file.read()
        l = r.split(",")
        return l


def file_open_incorrect(data):
    with codecs.open("incorrect/" + data, "r", "Shift-JIS", "ignore") as file:
        r = file.read()
        l = r.split(",")
        return l


def file_open_task(data):
    with codecs.open("task/" + data, "r", "Shift-JIS", "ignore") as file:
        r = file.read()
        l = r.split(",")
        return l


def main():
    import calc

    # csvfileのパス入力
    # print("Please write the directory path:")
    # path = input()
    correct_csv_file = [i for i in os.listdir(path="correct") if i[-3:] == "csv"]
    incorrect_csv_file = [i for i in os.listdir(path="incorrect") if i[-3:] == "csv"]
    task_csv_file = [i for i in os.listdir(path="task") if i[-3:] == "csv"]

    # 選択したいcorrect_csv_fileの番号
    for i, name in enumerate(correct_csv_file):
        print(i, name)

    print("--------------------------------------")
    choose_correct_csv = int(input("Please choose correct_csv_file number:"))

    # 選択したincorrect_csv_fileの番号
    for i, name in enumerate(incorrect_csv_file):
        print(i, name)

    print("--------------------------------------")
    choose_incorrect_csv = int(input("Please choose incorrect_csv_file number:"))

    # 選択したいtask_csv_fileの番号
    for i, name in enumerate(task_csv_file):
        print(i, name)

    print("--------------------------------------")
    choose_task_csv = int(input("Please choose task_csv_file number:"))

    correct = file_open_correct(correct_csv_file[choose_correct_csv])
    incorrect = file_open_incorrect(incorrect_csv_file[choose_incorrect_csv])
    task = file_open_task(task_csv_file[choose_task_csv])

    # print(correct)
    # print(incorrect)
    # print(task)
    # print(len(task))
    calc.calc(correct, incorrect, task)


if __name__ == "__main__":
    main()
