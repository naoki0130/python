import jtalk

text = input()
if text == "１":
    t = "お名前を教えてください"
elif text == "２":
    t = "性別はなんですか"
elif text == "３":
    t = "生年月日はなんですか"
elif text == "４":
    t = "年齢はいくつですか"
elif text == "５":
    t = "血液型はなんですか"
elif text == "６":
    t = "身長はなんセンチですか"
elif text == "７":
    t = "出身地はどこですか"
elif text == "８":
    t = "居住地はどこですか"
elif text == "９":
    t = "電話番号を教えてください"
elif text == "０":
    t = "趣味はなんですか"
elif text == "１１":
    t = "ありがとうございました"
elif text == "２２":
    t = "すみません　聞き取れませんでした　もう一度お願いします"
else:
    t = text + "ですね"

jtalk.jtalk(t)
