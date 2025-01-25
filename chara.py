""" base class for character creation/manipulation. This is supposed to make accessing members of cards easier """

import copy
import random
import _globals as _g
from kkloader import KoikatuCharaData, kk_Coordinate
from mother import Mother


class Child:

    def __init__(self, mother, output_name):
        if isinstance(mother, str): #and isinstance(father, str):
            pass
        else:
            raise TypeError("Both 'Mother' and 'Father' Files must be the filepath to the corresponding .png file in String Format")

        if not isinstance(output_name, str):
            raise TypeError("Parameter 'output_name' should be a string with the name the file should be called after creation")

        self.motherc = Mother("./pure.png")
        self.mother = KoikatuCharaData.load("./pure.png")
        # self.father = KoikatuCharaData.load(father)
        self.child = KoikatuCharaData()
        self.child.image = self.mother.image
        self.child.face_image = self.mother.image
        self.child.product_no = 100
        self.child.header = "【KoiKatuChara】".encode("utf-8")
        self.child.version = "0.0.0".encode("ascii")
        self.child.blockdata = copy.deepcopy(self.mother.blockdata)
        self.child["Custom"] = copy.deepcopy(self.mother["Custom"])
        self.child["Coordinate"] = copy.deepcopy(self.mother["Coordinate"])
        self.child["Parameter"] = copy.deepcopy(self.mother["Parameter"])
        self.child["Status"] = copy.deepcopy(self.mother["Status"])
        self.output_name = output_name



    def modify_value(self, base_value, percentage_change):
        min_value = base_value - (base_value * percentage_change)
        max_value = base_value + (base_value * percentage_change)

        new_value = random.uniform(min_value, max_value)

        return new_value

    def inherit_face(self):
        for i in _g.list_faceslider:
            currm = _g.getv(self.mother, i)
            if currm == 0.0:
                pass
            else:
                newitem = self.modify_value(currm, 0.5)
                _g.setv(self.child, i, newitem)

    def save(self):
        self.child.save(f"./{self.output_name}.png")
