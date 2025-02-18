import random
import copy
import chara
from kkloader import KoikatuCharaData
from functools import reduce
import _globals as _g

child = chara.Child(mother="pure", father="toshi", output_name="new_child")
child.inherit_face()
child.inherit_body()
child.inherit_hair()
child.save()

# c = KoikatuCharaData.load("./huh.png")
# c.save_json("whatever")

# print(child.mother.list_faceslider)
# face_width = ['Custom', 'face', 'shapeValueFace', 0]
# char1 = KoikatuCharaData.load("./pure.png")
# char2 = KoikatuCharaData.load("./braaaap.png")
# # for i in _g.list_faceslider:
# #     new = _g.getv(char1, i)
# #     print(new)

# old = _g.getv(char1, face_width)
# new = _g.getv(char2, face_width)
# print("old: ", old, " new: ", new)


# print("char1: ", _g.getv(char1, face_width))
# _g.setv(char1, face_width, 0.24)
# char1.save("test.png")
# char2 = KoikatuCharaData.load("./test.png")
# item = _g.getv(char2, face_width)
# print("char2: ", item)


# def get(d, path):
#     return reduce(lambda d, key: d[key] if isinstance(d, dict) else d[key], path, d)
# fwidth = get(char1, face_width)
# print(fwidth)

# from kkloader import KoikatuCharaData
# from mother import Mother

# fem = Mother("./pure.png")
# print(fem.lower_ear_shape)
# # fem = KoikatuCharaData.load("./pure.png")
# # # print(fem["Parameter"]["firstname"])
# # # print(fem["Parameter"]["lastname"])

# # mal = KoikatuCharaData.load("./toshi.png")
# # # fem.save_json("fem_other.json")
# # # print(mal["Parameter"]["firstname"])
# # # print(mal["Parameter"]["lastname"])
# # print(fem["Custom"]["face"]["shapeValueFace"][0])

# # # change = fem["Custom"]["hair"]["parts"][0]["baseColor"]
# # # change[0] = 0.7
# # # change[1] = 0.1
# # # change[2] = 0.1

# # # fem.save("./pure_modified.png")

# print(random.random())
# print(random.random())

# def modify_value(base_value, percentage_change):
#         min_value = base_value - (base_value * percentage_change)
#         max_value = base_value + (base_value * percentage_change)

#         new_value = random.uniform(min_value, max_value)

#         return new_value

# i = 0

# while i < 10000:
#     test = modify_value(0.50, 0.3)
#     print(test)
#     if test < 0.35 or test > 0.65:
#           raise RuntimeError
#     i += 1