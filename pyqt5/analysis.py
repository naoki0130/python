import pandas as pd
from scipy import signal, stats
import os
import codecs
import csv
import pprint
import calc

# import calc

# csv_file_open
def file_open_correct(person, data):
    with codecs.open(person + "/correct/" + data, "r", "Shift-JIS", "ignore") as file:
        r = file.read()
        l = r.split(",")
        return l


def file_open_incorrect(person, data):
    with codecs.open(person + "/incorrect/" + data, "r", "Shift-JIS", "ignore") as file:
        r = file.read()
        l = r.split(",")
        return l


def file_open_task(person, data):
    with codecs.open(person + "/task/" + data, "r", "Shift-JIS", "ignore") as file:
        r = file.read()
        l = r.split(",")
        return l


def file_open_time(person, data):
    with codecs.open(person + "/time/" + data, "r", "Shift-JIS", "ignore") as file:
        r = file.read()
        l = r.split(",")
        return l


def dic(file):
    task = []
    j = []
    for i, v in enumerate(file, 1):
        if "incorrect" in v:
            task.append("incorrect")
            j.append(i)
        else:
            task.append("correct")
            j.append(i)

    task_dic = dict(zip(j, task))
    return task_dic


def dic_update(task, correct, incorrect):
    diction = task

    for i in correct:
        if diction[int(i)] == "correct":
            diction[int(i)] = "o"
        else:
            diction[int(i)] = "x"

    for i in incorrect:
        if diction[int(i)] == "incorrect":
            diction[int(i)] = "o"
        else:
            diction[int(i)] = "x"

    return diction


def main():

    # csvfileのパス入力
    # print("Please write the directory path:")
    # path = input()
    print("Please write initial:")
    path = input()
    correct_csv_file = [
        i for i in os.listdir(path=path + "/correct") if i[-3:] == "csv"
    ]
    incorrect_csv_file = [
        i for i in os.listdir(path=path + "/incorrect") if i[-3:] == "csv"
    ]
    task_csv_file = [i for i in os.listdir(path=path + "/task") if i[-3:] == "csv"]

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

    correct = file_open_correct(path, correct_csv_file[choose_correct_csv])
    incorrect = file_open_incorrect(path, incorrect_csv_file[choose_incorrect_csv])
    task = file_open_task(path, task_csv_file[choose_task_csv])
    dictionary = dic(task)
    resalt = dic_update(dictionary, correct, incorrect)

    print("--------------------------------------")
    print("問題番号：正誤（*文字の場合はエラー）")
    print()
    for i in resalt:
        print(str(i) + ":" + str(resalt[i]))

    # calc_task_ans = calc.calc_task_ans(resalt)


if __name__ == "__main__":
    main()
