import jtalk
import time
import talk

text_box = ["お名前を教えてください", "性別はなんですか", "生年月日はなんですか", "年齢はいくつですか", "血液型はなんですか", "ありがとうございました"]


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
