import os


def calc_task_ans(dic):
    correct = 0
    incorrect = 0
    task = len(dic)

    for i in dic:
        if dic[i] == "o":
            correct += 1
        elif dic[i] == "x":
            incorrect += 1
        else:
            incorrect += 1

    resalt = round((correct / task) * 100, 1)

    return resalt


def calc_task_mean_time(time):
    total = 0
    time_sum = 0

    for i in time:
        i = float(i)
        total += i
        time_sum += 1

    mean_time = round(total / time_sum, 4)
    mean_time = mean_time * 1000

    return mean_time

