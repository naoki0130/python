import jtalk
import time


def error_return(e):
    if e == "０":
        return "すみません　聞き取れませんでした　もう一度お願いします"
    else:
        return e + "ですか"


def say_confirm():
    t = input("input confirm text or ０:")
    text = error_return(t)
    return text


def roop_or_not(t):
    i = 0
    t = t
    while i < 1:
        if t == "すみません　聞き取れませんでした　もう一度お願いします":
            jtalk.jtalk(t)
            t = say_confirm()
        else:
            jtalk.jtalk(t)
            c = input("y or n:")
            if c == "y":
                i += 1
                time.sleep(1)
            else:
                t = say_confirm()


text_box = ["お名前を教えてください", "性別はなんですか", "生年月日はなんですか", "年齢はいくつですか", "血液型はなんですか", "ありがとうございました"]


def main():
    jtalk.jtalk(text_box[0])
    text = say_confirm()
    roop_or_not(text)

    jtalk.jtalk(text_box[1])
    text = say_confirm()
    roop_or_not(text)

    jtalk.jtalk(text_box[2])
    text = say_confirm()
    roop_or_not(text)

    jtalk.jtalk(text_box[3])
    text = say_confirm()
    roop_or_not(text)

    jtalk.jtalk(text_box[4])
    text = say_confirm()
    roop_or_not(text)

    jtalk.jtalk(text_box[5])


if __name__ == "__main__":
    main()
