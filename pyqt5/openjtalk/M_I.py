import jtalk

text = input()
if text == "１":
    t = "あなたについて教えてください"
elif text == "２":
    t = "性別はなんですか"
elif text == "３":
    t = "生年月日はいつですか"
elif text == "４":
    t = "年齢はいくつですか"
elif text == "５":
    t = "もう１つあなたについて教えてください"
elif text == "６":
    t = "血液型はなんですか"
elif text == "７":
    t = "身長はなんセンチですか"
elif text == "８":
    t = "何人家族ですか"
elif text == "９":
    t = "もう１つあなたについて教えてください"
elif text == "０":
    t = "趣味はなんですか"
elif text == "１１":
    t = "ありがとうございました"
elif text == "２２":
    t = "すみません　聞き取れませんでした　もう一度お願いします"
else:
    t = text

jtalk.jtalk(t)
