import jtalk

text = input()
if text == "１":
    t = "あなたについて教えてください"
elif text == "２":
    t = "性別はなんですか"
elif text == "３":
    t = "もう１つあなたについて教えてください"
elif text == "４":
    t = "血液型はなんですか"
elif text == "５":
    t = "もう１つあなたについて教えてください"
elif text == "６":
    t = "ありがとうございました"
elif text == "７":
    t = "すみません　聞き取れませんでした　もう一度お願いします"
else:
    t = text

jtalk.jtalk(t)
