""" base class for character creation/manipulation. This is supposed to make accessing members of cards easier """

import copy
import random
from kkloader import KoikatuCharaData
import _globals as _g
from mother import Mother


class Child:

    def __init__(self, mother, output_name):
        if not isinstance(mother, str): #and isinstance(father, str):
            raise TypeError("Both 'Mother' and 'Father' Files must be the filepath to the corresponding .png file in String Format")

        if not isinstance(output_name, str):
            raise TypeError("Parameter 'output_name' should be a string with the name the file should be called after creation")

        self.motherc = Mother("./Nakano-Yotsuba.png")
        self.mother = KoikatuCharaData.load("./Nakano-Yotsuba.png")
        # self.father = KoikatuCharaData.load(father)
        self.child = KoikatuCharaData()
        self.child.image = self.mother.image
        self.child.face_image = self.mother.image
        self.child.product_no = 100
        self.child.header = "【KoiKatuChara】".encode("utf-8")
        self.child.version = "0.0.0".encode("ascii")
        self.child.blockdata = copy.deepcopy(self.mother.blockdata)
        if self.mother["KKEx"]:
            self.child["KKEx"] = copy.deepcopy(self.mother["KKEx"])
        self.child["Custom"] = copy.deepcopy(self.mother["Custom"])
        self.child["Coordinate"] = copy.deepcopy(self.mother["Coordinate"])
        self.child["Parameter"] = copy.deepcopy(self.mother["Parameter"])
        self.child["Status"] = copy.deepcopy(self.mother["Status"])
        self.output_name = output_name


    # ---------------------------------------------------------------------------------------------
    def modify_value(self, base_value, percentage_change):
        """ change current value randomly within a certain range """
        min_value = base_value - (base_value * percentage_change)
        max_value = base_value + (base_value * percentage_change)
        new_value = random.uniform(min_value, max_value)

        return new_value

    # ---------------------------------------------------------------------------------------------
    def inherit_face(self):
        """ take faceslider values of parent characters, modify and save as child facesliders """

        # loop through facesliders and modify all values to a random degree (currently 50% up or down from base)
        for i in _g.list_faceslider:
            currm = _g.getv(self.mother, i)
            if currm == 0.0:
                continue
            # changing the randomization of head size
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][1]:
                newitem = self.modify_value(currm, 0.2)
                _g.setv(self.child, i, newitem)
            else:
                newitem = self.modify_value(currm, 0.5)
                # set resulting value as corresponding faceslider value of child
                _g.setv(self.child, i, newitem)

    # ---------------------------------------------------------------------------------------------
    def inherit_body(self):
        """ take bodyslider values of parent characters, modify and save as child bodysliders """

        # loop through bodysliders and modify all values to a random degree
        for i in _g.list_bodyslider:
            currm = _g.getv(self.mother, i)
            if currm == 0.0:
                continue
            # changing the randomization of breast size
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][4]:
                newitem = self.modify_value(currm, 0.5)
                print(newitem)
                _g.setv(self.child, i, newitem)
                continue
            # changing the randomization of butt angle (can get really fucked up)
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][27]:
                newitem = self.modify_value(currm, 0.15)
                _g.setv(self.child, i, newitem)
                continue
            else: 
                newitem = self.modify_value(currm, 0.3)
                # set resulting value as corresponding bodyslider value of child
                _g.setv(self.child, i, newitem)

    # ---------------------------------------------------------------------------------------------
    def save(self):
        """ call .save() method of KoikatuCharaData with desired output name """
        self.child.save(f"./{self.output_name}.png")
