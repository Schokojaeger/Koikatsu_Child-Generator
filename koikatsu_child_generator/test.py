""" test class for creating new characters """

#import random
#import copy
from koikatsu_child_generator import chara
#from kkloader import KoikatuCharaData
#from functools import reduce
#import koikatsu_child_generator.constants as constants

child = chara.Child(mother="", father="", output_name="new_child")
child.inherit_face()
child.inherit_body(True)
child.inherit_hair(True)
child.inherit_eyes(True)
child.save()
