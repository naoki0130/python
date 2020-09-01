import os
import calc
import analysis


def main():
    print("Please write initial:")
    path = input()
    time_csv_file = [i for i in os.listdir(path=path + "/time") if i[-3:] == "csv"]

    for i, name in enumerate(time_csv_file):
        print(i, name)

    print("--------------------------------------")
    choose_time_csv = int(input("Please choose time_csv_file number:"))

    time = analysis.file_open_time(path, time_csv_file[choose_time_csv])

    mean_time = calc.calc_task_mean_time(time)
    print()
    print("平均解答時間（ms）：" + str(mean_time))


if __name__ == "__main__":
    main()
