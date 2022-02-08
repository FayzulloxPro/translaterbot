import googletrans
from googletrans import LANGUAGES, Translator
translater = Translator()
# print(googletrans.LANGUAGES)
text1 = "mening ismim Fayzullox"
print(translater.detect(text1))




translation = translater.translate(text1, src="uz", dest="en")
print(translation)
# a = str(translation)
# detection = translater.detect(text1)
# det_make_str = str(detection)
# pos = det_make_str.find(",")
#
# source = det_make_str[14 : pos]
#
# print(detection)
# print(det_make_str)
# print(source)

# pos_1 = a.find("text=") + 5
# pos_2 = a.find("pronunciation=", pos_1) - 2
# print(pos_1)
# print(pos_2)
# print(a[pos_1 : pos_2])
#
