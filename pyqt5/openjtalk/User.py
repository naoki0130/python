import jtalk
import time
import talk

text_box = ["あなたについて教えてください", "２つ目の情報はなんですか", "３つ目の情報はなんですか", "4つ目の情報はなんですか",
            "５つ目の情報はなんですか", "ありがとうございました"]

jtalk.jtalk(text_box[0])
text = talk.say_confirm()
talk.roop_or_not(text)


jtalk.jtalk(text_box[1])
text = talk.say_confirm()
talk.roop_or_not(text)

jtalk.jtalk(text_box[2])
text = talk.say_confirm()
talk.roop_or_not(text)

jtalk.jtalk(text_box[3])
text = talk.say_confirm()
talk.roop_or_not(text)

jtalk.jtalk(text_box[4])
text = talk.say_confirm()
talk.roop_or_not(text)

jtalk.jtalk(text_box[5])
