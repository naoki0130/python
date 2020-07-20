import os

# from analysis import file_open_task


def task(task):
    task_list = []
    for i in task:
        if i == "left_L_correct":
            task_list.append("correct")
        elif i == "right_R_correct":
            task_list.append("correct")
        elif i == "right_L_incorrect":
            task_list.append("incorrect")
        else:
            task_list.append("incorrect")
    return task_list


def calc(co, inco, t):
    co = len(co)
    inco = len(inco)
    t = task(t)
    t_len = len(t)
    task_co = 0
    task_inco = 0
    for i in t:
        if i == "correct":
            task_co += 1
        else:
            task_inco += 1
    correct = task_co - co
    incorrect = task_inco - inco
    h = correct + incorrect
    result = (t_len - h) / t_len * 100
    print(result)


# def main():
#    task_csv_file = [i for i in os.listdir(path="task") if i[-3:] == "csv"]
#
#    # 選択したいtask_csv_fileの番号
#    for i, name in enumerate(task_csv_file):
#        print(i, name)
#
#    print("--------------------------------------")
#    choose_task_csv = int(input("Please choose task_csv_file number:"))
#
#    task = task(file_open_task((task_csv_file[choose_task_csv])))
#    print(task)
#
#
# if __name__ == "__main__":
#    main()
