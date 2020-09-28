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
    t = "ありがとうございました"
elif text == "７":
    t = "すみません　聞き取れませんでした　もう一度お願いします"
else:
    t = text + "ですか"

jtalk.jtalk(t)
