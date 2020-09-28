import jtalk

text = input()
if text == "１":
    t = "あなたについて教えてください"
elif text == "２":
    t = "２つ目の情報はなんですか"
elif text == "３":
    t = "３つ目の情報はなんですか"
elif text == "４":
    t = "4つ目の情報はなんですか"
elif text == "５":
    t = "５つ目の情報はなんですか"
elif text == "６":
    t = "ありがとうございました"
elif text == "７":
    t = "すみません　聞き取れませんでした　もう一度お願いします"
else:
    t = text

jtalk.jtalk(t)
